// ─── PIXEL PARTICLE SYSTEM ───
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
const W = canvas.width, H = canvas.height;

let particles = [];
const PHASE_CHAOS = 0, PHASE_FORMING = 1, PHASE_FORMED = 2, PHASE_SCATTER = 3;
let phase = PHASE_CHAOS;
let phaseTimer = 0;
const FORM_DURATION = 200;
const HOLD_DURATION = 400;
const SCATTER_DURATION = 150;
const CHAOS_DURATION = 400;

// Track mouse position
let mouse = { x: -1000, y: -1000 };
if (canvas) {
  canvas.addEventListener('mousemove', e => {
      const rect = canvas.getBoundingClientRect();
      mouse.x = (e.clientX - rect.left) * (W / rect.width);
      mouse.y = (e.clientY - rect.top) * (H / rect.height);
  });
  canvas.addEventListener('mouseleave', () => {
      mouse.x = -1000;
      mouse.y = -1000;
  });
}

function initParticles() {
    if (typeof FACEPIXELS === 'undefined') return;
    const data = FACEPIXELS;
    const grid = data.grid || 45;
    const scale = 1.0;
    const cellW = (W * scale) / grid;
    const cellH = (H * scale) / grid;
    const offsetX = (W - W * scale) / 2;
    const offsetY = (H - H * scale) / 2;

    particles = data.particles.map(p => {
        const tx = offsetX + p.x * W * scale + cellW/2;
        const ty = offsetY + p.y * H * scale + cellH/2;
        return {
            x: Math.random() * W, y: Math.random() * H,
            tx, ty, sx: 0, sy: 0,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2,
            r: p.r, g: p.g, b: p.b,
            size: 4 + Math.random() * 2
        };
    });
    particles.forEach(p => {
        p.sx = Math.random() * W;
        p.sy = Math.random() * H;
    });
}

function lerp(a, b, t) { return a + (b - a) * t; }

function update() {
    phaseTimer++;
    if (phase === PHASE_CHAOS && phaseTimer > CHAOS_DURATION) {
        phase = PHASE_FORMING; phaseTimer = 0;
        particles.forEach(p => { p.sx = p.x; p.sy = p.y; });
    } else if (phase === PHASE_FORMING && phaseTimer > FORM_DURATION) {
        phase = PHASE_FORMED; phaseTimer = 0;
    } else if (phase === PHASE_FORMED && phaseTimer > HOLD_DURATION) {
        phase = PHASE_SCATTER; phaseTimer = 0;
    } else if (phase === PHASE_SCATTER && phaseTimer > SCATTER_DURATION) {
        phase = PHASE_CHAOS; phaseTimer = 0;
    }

    const t = phaseTimer;
    particles.forEach(p => {
        let baseX, baseY;
        if (phase === PHASE_CHAOS) {
            p.vx += (Math.random() - 0.5) * 0.5;
            p.vy += (Math.random() - 0.5) * 0.5;
            p.vx *= 0.96;
            p.vy *= 0.96;
            baseX = p.x + p.vx;
            baseY = p.y + p.vy;
            if (baseX < 0 || baseX > W) p.vx *= -0.5;
            if (baseY < 0 || baseY > H) p.vy *= -0.5;
            baseX = Math.max(0, Math.min(W, baseX));
            baseY = Math.max(0, Math.min(H, baseY));
        } else if (phase === PHASE_FORMING) {
            const progress = Math.min(t / FORM_DURATION, 1);
            const ease = 1 - Math.pow(1 - progress, 3);
            baseX = lerp(p.sx, p.tx, ease);
            baseY = lerp(p.sy, p.ty, ease);
        } else if (phase === PHASE_FORMED) {
            const breathe = Math.sin(t * 0.02 + p.tx * 0.1) * 0.3;
            baseX = p.tx + breathe;
            baseY = p.ty + Math.cos(t * 0.02 + p.ty * 0.1) * 0.3;
        } else if (phase === PHASE_SCATTER) {
            const progress = Math.min(t / SCATTER_DURATION, 1);
            const ease = progress * progress;
            baseX = lerp(p.tx, p.sx, ease);
            baseY = lerp(p.sy, p.sy, ease);
        }

        // Apply mouse interaction (push away) - OPTIMIZED: Avoid square root if far away
        const dx = baseX - mouse.x;
        const dy = baseY - mouse.y;
        const distSq = dx * dx + dy * dy;
        const maxDist = 45;
        const maxDistSq = 2025; // 45 * 45
        if (distSq < maxDistSq) {
            const dist = Math.sqrt(distSq);
            const force = (maxDist - dist) / maxDist;
            const pushX = (dx / (dist || 1)) * force * 15;
            const pushY = (dy / (dist || 1)) * force * 15;
            p.x = baseX + pushX;
            p.y = baseY + pushY;
        } else {
            p.x = baseX;
            p.y = baseY;
        }
    });
}

function draw() {
    ctx.clearRect(0, 0, W, H);
    const isFormed = phase === PHASE_FORMED;
    const isForming = phase === PHASE_FORMING;
    const isScatter = phase === PHASE_SCATTER;
    const prog = Math.min(phaseTimer / FORM_DURATION, 1);
    const scatterProg = Math.min(phaseTimer / SCATTER_DURATION, 1);

    particles.forEach(p => {
        let sz, alpha;
        if (isFormed) { sz = 4.5; alpha = 1.0; }
        else if (isForming) { sz = 2.5 + prog * 3; alpha = 0.3 + prog * 0.7; }
        else if (isScatter) { sz = 4.5 * (1 - scatterProg * 0.5); alpha = 1.0 - scatterProg * 0.8; }
        else { sz = 2; alpha = 0.2; }

        ctx.beginPath();
        ctx.arc(p.x, p.y, sz, 0, Math.PI * 2);
        if (isFormed || isForming) { ctx.fillStyle = `rgba(${p.r},${p.g},${p.b},${alpha})`; }
        else if (isScatter) {
            const gray = Math.round(0.3 * p.r + 0.59 * p.g + 0.11 * p.b);
            const mix = scatterProg;
            const r = Math.round(p.r + (gray - p.r) * mix);
            const g = Math.round(p.g + (gray - p.g) * mix);
            const b = Math.round(p.b + (gray - p.b) * mix);
            ctx.fillStyle = `rgba(${r},${g},${b},${alpha})`;
        } else { ctx.fillStyle = `rgba(148,163,184,${alpha})`; }
        ctx.fill();
    });
}

function animate() {
    update();
    draw();
    requestAnimationFrame(animate);
}

if (canvas) {
  initParticles();
  animate();
}

// ─── FADE-IN ON SCROLL ───
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.1 });
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// Smooth scroll & Tab-like expand
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    const targetId = a.getAttribute('href');
    const t = document.querySelector(targetId);
    if(t) {
      const isCollapsed = t.classList.contains('collapsed');
      
      // Close all blocks (home and sections)
      document.querySelectorAll('header.hero, section').forEach(b => {
        b.classList.add('collapsed');
      });
      
      if (isCollapsed) {
        t.classList.remove('collapsed');
        t.scrollIntoView({behavior:'smooth', block:'start'});
      } else {
        // If it was already open, keep it open!
        t.classList.remove('collapsed');
      }
    }
  });
});

// ─── PROJECTS FILTERING ───
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    // Remove active class from all buttons
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    // Add active class to clicked button
    btn.classList.add('active');
    
    const filter = btn.getAttribute('data-filter');
    const projects = document.querySelectorAll('.project-card-wrapper');
    
    projects.forEach(p => {
      const cat = p.getAttribute('data-category');
      if (filter === 'all' || cat === filter) {
        p.classList.remove('hidden');
      } else {
        p.classList.add('hidden');
      }
    });
  });
});
