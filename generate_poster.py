import os
import requests

def generate_qr_codes():
    print("Generating QR codes for Portfolio Page...")
    urls = {
        "website": "https://fil-m.github.io/portfolio-page/",
        "organizer": "https://t.me/robosapiens8"
    }
    
    # Try using qrcode library if installed
    try:
        import qrcode
        print("Using local 'qrcode' library.")
        for name, url in urls.items():
            qr = qrcode.QRCode(version=1, box_size=10, border=1)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"assets/qr_{name}.png")
            print(f"Generated assets/qr_{name}.png")
    except ImportError:
        print("Local 'qrcode' library not found. Fetching from QR Server API...")
        os.makedirs("assets", exist_ok=True)
        for name, url in urls.items():
            api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url}"
            try:
                response = requests.get(api_url, timeout=10)
                if response.status_code == 200:
                    with open(f"assets/qr_{name}.png", "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded assets/qr_{name}.png")
                else:
                    print(f"Failed to fetch QR code for {name}: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error fetching QR code for {name}: {e}")

def create_html_poster():
    print("Creating HTML poster...")
    html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тарас Москаленко — Афіша А4</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            color: #000000;
            background: #ffffff;
            line-height: 1.4;
            padding: 0;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        
        @page {
            size: A4;
            margin: 12mm 15mm;
        }
        
        .poster-container {
            width: 100%;
            max-width: 210mm;
            min-height: 297mm;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* Header styling */
        .header {
            text-align: center;
            border-bottom: 3px solid #000;
            padding-bottom: 8px;
            margin-bottom: 16px;
        }
        .header-badge {
            display: inline-block;
            border: 2px solid #000;
            padding: 4px 12px;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        .header h1 {
            font-size: 38px;
            font-weight: 900;
            letter-spacing: -1px;
            text-transform: uppercase;
            line-height: 1.1;
            margin-bottom: 4px;
        }
        .header h1 span {
            background: #000;
            color: #fff;
            padding: 0 8px;
            display: inline-block;
        }
        .header .tagline {
            font-size: 16px;
            font-weight: 600;
            margin-top: 4px;
        }

        /* Main content */
        .main-content {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .section-box {
            border: 2px solid #000;
            padding: 12px 16px;
            background: #ffffff;
        }
        
        .section-title {
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            border-bottom: 2px solid #000;
            padding-bottom: 2px;
            margin-bottom: 8px;
            display: inline-block;
        }

        .core-text {
            font-size: 13.5px;
            line-height: 1.45;
            margin-bottom: 8px;
        }

        /* Projects Grid */
        .projects-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px 20px;
        }
        .project-item {
            font-size: 12.5px;
            line-height: 1.35;
        }
        .project-item strong {
            display: block;
            font-size: 13.5px;
            font-weight: 700;
            margin-bottom: 2px;
        }

        /* Skills Tags */
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 4px;
        }
        .skill-tag {
            border: 1px solid #000;
            padding: 2px 10px;
            font-size: 11px;
            font-weight: 600;
            background: #fdfdfd;
        }

        /* Disclaimer Box */
        .disclaimer-box {
            border: 2px dashed #000;
            background: #fdfdfd;
            padding: 12px;
            text-align: center;
        }
        .disclaimer-box h3 {
            font-size: 15px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .disclaimer-box p {
            font-size: 12.5px;
            font-weight: 600;
            line-height: 1.3;
        }

        /* QR section */
        .qr-section {
            border-top: 2px solid #000;
            padding-top: 12px;
            margin-top: 10px;
        }
        .qr-title {
            text-align: center;
            font-size: 14px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .qr-grid {
            display: flex;
            justify-content: center;
            gap: 60px;
        }
        .qr-card {
            text-align: center;
            max-width: 150px;
        }
        .qr-image-wrapper {
            border: 2px solid #000;
            padding: 4px;
            background: #fff;
            display: inline-block;
            margin-bottom: 4px;
        }
        .qr-card img {
            width: 100px;
            height: 100px;
            display: block;
        }
        .qr-card h4 {
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .qr-card p {
            font-size: 10.5px;
            color: #444;
            line-height: 1.2;
        }

        .footer-note {
            text-align: center;
            font-size: 11px;
            font-weight: 600;
            margin-top: 12px;
            border-top: 1px solid #ddd;
            padding-top: 6px;
        }
        .impressum {
            font-size: 9px;
            font-weight: normal;
            color: #666;
            display: block;
            margin-top: 4px;
        }

        /* Print controls banner */
        .no-print-banner {
            background: #f0f0f0;
            border: 1px solid #ccc;
            padding: 12px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 14px;
        }
        .no-print-banner button {
            background: #000;
            color: #fff;
            border: none;
            padding: 8px 16px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .no-print-banner button:hover {
            background: #333;
        }

        @media print {
            .no-print-banner {
                display: none !important;
            }
            body {
                padding: 0;
            }
            .poster-container {
                min-height: auto;
            }
        }
    </style>
</head>
<body>

    <div class="no-print-banner">
        <strong>Афіша портфоліо підготовлена до друку на форматі A4 (чорно-біла).</strong><br>
        Відкрийте цю сторінку в браузері, натисніть кнопку нижче або комбінацію клавіш <strong>Ctrl + P</strong> і виберіть принтер або збереження в PDF.<br>
        <button onclick="window.print()">Друк / Зберегти як PDF</button>
    </div>

    <div class="poster-container">
        <div class="header">
            <div class="header-badge">Портфоліо та суспільні проекти</div>
            <h1>Тарас Москаленко</h1>
            <p class="tagline">Спеціаліст з розвитку. Людина. Творець.</p>
        </div>

        <div class="main-content">
            <div class="section-box">
                <div class="section-title">Хто я та чим займаюсь?</div>
                <p class="core-text">Допомагаю людям робити крок від «хочу» до «роблю» через анімацію, технології, психологію, творчість і волонтерство. Моя мета — об'єднувати знання з різних дисциплін для вирішення реальних завдань спільноти.</p>
            </div>

            <div class="section-box">
                <div class="section-title">Ключові волонтерські та соціальні проекти</div>
                <div class="projects-grid">
                    <div class="project-item">
                        <strong>★ Дія до мрії</strong>
                        Безкоштовна ініціатива підтримки для старту ваших ідей. Напарник, що допомагає зробити перший практичний крок.
                    </div>
                    <div class="project-item">
                        <strong>🖨️ Стіна 3D друкарня</strong>
                        Волонтерська 3D-ферма в Карлсруе з 8 принтерів. Безкоштовний друк деталей для протезів та медицини для України.
                    </div>
                    <div class="project-item">
                        <strong>🎬 Animation Mentors</strong>
                        Освітня ініціатива: навчання дорослих створенню мультиків з дітьми для розвитку проектного мислення.
                    </div>
                    <div class="project-item">
                        <strong>🎨 Арт Пікнік</strong>
                        Творчі сімейні зустрічі просто неба: створення аматорських кліпів та стопмоушен анімації.
                    </div>
                </div>
            </div>

            <div class="section-box">
                <div class="section-title">Практичний досвід та експертиза</div>
                <div class="projects-grid">
                    <div class="project-item">
                        <strong>💻 IT, AI та автоматизація</strong>
                        Створення сайтів, програмування ігор, розробка multi-agent AI-систем та ботів автоматизації.
                    </div>
                    <div class="project-item">
                        <strong>🧠 Психологія та дослідження</strong>
                        Аналіз когнітивних функцій (фізіологія ВНД, нейрональна парадигма, біхевіоризм, скринінг).
                    </div>
                </div>
                <div class="skills-container">
                    <span class="skill-tag">🌱 Розвиток</span>
                    <span class="skill-tag">🎬 Анімація</span>
                    <span class="skill-tag">🖨️ 3D-друк</span>
                    <span class="skill-tag">🎮 GameDev</span>
                    <span class="skill-tag">🤖 AI</span>
                    <span class="skill-tag">🧠 Психологія</span>
                    <span class="skill-tag">🎵 Музика</span>
                    <span class="skill-tag">🏔️ Походи</span>
                </div>
            </div>

            <div class="disclaimer-box">
                <h3>Відкритий до співпраці та обміну досвідом</h3>
                <p>Люди завжди важливіші за технології. Якщо ви хочете запустити спільний проект, потребуєте допомоги у розвитку дитини або плануєте відкрити волонтерську 3D-ферму — вийдемо на зв'язок!</p>
            </div>
        </div>

        <div class="qr-section">
            <div class="qr-title">Переглянути моє повне портфоліо та написати:</div>
            <div class="qr-grid">
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_website.png" alt="QR Website">
                    </div>
                    <h4>Сайт-портфоліо</h4>
                    <p>Повний список проектів, коду, музики та контактів</p>
                </div>
                
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_organizer.png" alt="QR Telegram Contact">
                    </div>
                    <h4>Telegram зв'язок</h4>
                    <p>Напишіть мені особисто: @robosapiens8</p>
                </div>
            </div>
        </div>

        <div class="footer-note">
            Тарас Москаленко · Людина. Творець. · Karlsruhe
            <span class="impressum">Impressum: Taras Moskalenko, Stresemannstraße 5, 76187 Karlsruhe | moskalenko.t.o@gmail.com</span>
        </div>
    </div>

</body>
</html>
"""
    with open("poster.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Created poster.html")

def create_pdf_poster():
    print("Creating PDF poster...")
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError:
        print("Reportlab not available. Cannot generate PDF directly. Use HTML poster and print as PDF.")
        return

    # Check for Arial font on Windows
    arial_path = "C:\\Windows\\Fonts\\arial.ttf"
    arial_bold_path = "C:\\Windows\\Fonts\\arialbd.ttf"
    
    if os.path.exists(arial_path) and os.path.exists(arial_bold_path):
        pdfmetrics.registerFont(TTFont('Arial', arial_path))
        pdfmetrics.registerFont(TTFont('Arial-Bold', arial_bold_path))
        FONT_NORMAL = 'Arial'
        FONT_BOLD = 'Arial-Bold'
        print("Using system Arial font for Cyrillic support.")
    else:
        FONT_NORMAL = 'Helvetica'
        FONT_BOLD = 'Helvetica-Bold'
        print("Arial font not found. Falling back to Helvetica (Cyrillic characters might not render).")

    doc = SimpleDocTemplate(
        "taras_moskalenko_portfolio_a4.pdf",
        pagesize=A4,
        rightMargin=15*mm,
        leftMargin=15*mm,
        topMargin=12*mm,
        bottomMargin=12*mm
    )

    styles = getSampleStyleSheet()

    # Define custom styles
    title_p1_style = ParagraphStyle('T1', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=28, leading=32, alignment=2)
    title_p2_style = ParagraphStyle('T2', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=28, leading=32, alignment=1)
    
    badge_style = ParagraphStyle('Badge', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10, leading=12, alignment=1)
    tagline_style = ParagraphStyle('Tagline', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=12, leading=15, alignment=1)
    
    sec_title_style = ParagraphStyle('SecTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=11.5, leading=13.5, spaceAfter=3)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11)
    core_text_style = ParagraphStyle('CoreTextCustom', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=9, leading=12)
    
    detail_bold_style = ParagraphStyle('DetailBold', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=11)
    detail_body_style = ParagraphStyle('DetailBody', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11)
    
    highlight_title_style = ParagraphStyle('HighlightTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=11.5, leading=13.5, alignment=1, spaceAfter=2)
    highlight_body_style = ParagraphStyle('HighlightBody', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=12, alignment=1)
    
    qr_title_style = ParagraphStyle('QRTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10, leading=12, alignment=1)
    qr_label_style = ParagraphStyle('QRLabel', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=11, alignment=1)
    qr_desc_style = ParagraphStyle('QRDesc', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8, leading=9.5, alignment=1)
    
    footer_style = ParagraphStyle('FooterStyle', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=7.5, leading=9, alignment=1, textColor=colors.HexColor('#555555'))

    story = []

    # 1. Header Badge
    badge_p = Paragraph("ПОРТФОЛІО ТА СУСПІЛЬНІ ПРОЕКТИ", badge_style)
    badge_table = Table([[badge_p]], colWidths=[80*mm])
    badge_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    badge_table.hAlign = 'CENTER'
    story.append(badge_table)
    story.append(Spacer(1, 3*mm))

    # 2. Main Title: ТАРАС МОСКАЛЕНКО
    title_style = ParagraphStyle('MainTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=26, leading=30, alignment=1)
    story.append(Paragraph("ТАРАС МОСКАЛЕНКО", title_style))
    story.append(Spacer(1, 3*mm))

    # Tagline
    story.append(Paragraph("Спеціаліст з розвитку. Людина. Творець.", tagline_style))
    story.append(Spacer(1, 2.5*mm))

    # Thin line under header
    line_table = Table([[""]], colWidths=[176*mm], rowHeights=[2])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 2, colors.black),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 4*mm))

    # 3. Section 1: About me
    sec1_content = [
        [Paragraph("ХТО Я ТА ЧИМ ЗАЙМАЮСЬ?", sec_title_style)],
        [Paragraph("Допомагаю людям робити крок від «хочу» до «роблю» через анімацію, технології, психологію, творчість і волонтерство. Моя мета — об'єднувати знання з різних дисциплін для вирішення реальних завдань спільноти.", core_text_style)]
    ]
    sec1_table = Table(sec1_content, colWidths=[176*mm])
    sec1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
    ]))
    sec1_table.hAlign = 'CENTER'
    story.append(sec1_table)
    story.append(Spacer(1, 4*mm))

    # 4. Section 2: Projects (2x2 grid)
    sec2_content = [
        [Paragraph("КЛЮЧОВІ ВОЛОНТЕРСЬКІ ТА СОЦІАЛЬНІ ПРОЕКТИ", sec_title_style), ""],
        [
            Paragraph("<b>★ Дія до мрії</b><br/>Безкоштовна ініціатива підтримки для старту ваших ідей. Напарник, що допомагає зробити перший практичний крок.", body_style),
            Paragraph("<b>🖨️ Стіна 3D друкарня</b><br/>Волонтерська 3D-ферма в Карлсруе з 8 принтерів. Безкоштовний друк деталей для протезів та медицини для України.", body_style)
        ],
        [
            Paragraph("<b>🎬 Animation Mentors</b><br/>Освітня ініціатива: навчання дорослих створенню мультиків з дітьми для розвитку проектного мислення.", body_style),
            Paragraph("<b>🎨 Арт Пікнік</b><br/>Творчі сімейні зустрічі просто неба: створення аматорських кліпів та стопмоушен анімації.", body_style)
        ]
    ]
    sec2_table = Table(sec2_content, colWidths=[88*mm, 88*mm])
    sec2_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-2), 4),
    ]))
    sec2_table.hAlign = 'CENTER'
    story.append(sec2_table)
    story.append(Spacer(1, 4*mm))

    # 5. Section 3: Tech and Science Expertise
    skills_list_p = Paragraph("🌱 Розвиток  |  🎬 Анімація  |  🖨️ 3D-друк  |  🎮 GameDev  |  🤖 AI  |  🧠 Психологія  |  🎵 Музика  |  🏔️ Походи", detail_bold_style)
    sec3_content = [
        [Paragraph("ПРАКТИЧНИЙ ДОСВІД ТА ЕКСПЕРТИЗА", sec_title_style), ""],
        [
            Paragraph("<b>💻 IT, AI та автоматизація</b><br/>Створення сайтів, програмування ігор, розробка multi-agent AI-систем та ботів автоматизації.", body_style),
            Paragraph("<b>🧠 Психологія та дослідження</b><br/>Аналіз когнітивних функцій (фізіологія ВНД, нейрональна парадигма, біхевіоризм, скринінг).", body_style)
        ],
        [skills_list_p, ""]
    ]
    sec3_table = Table(sec3_content, colWidths=[88*mm, 88*mm])
    sec3_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('SPAN', (0,2), (1,2)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-2), 4),
    ]))
    sec3_table.hAlign = 'CENTER'
    story.append(sec3_table)
    story.append(Spacer(1, 4*mm))

    # 6. Disclaimer Box
    disclaimer_p1 = Paragraph("ВІДКРИТИЙ ДО СПІВПРАЦІ ТА ОБМІНУ ДОСВІДОМ", highlight_title_style)
    disclaimer_p2 = Paragraph("Люди завжди важливіші за технології. Якщо ви хочете запустити спільний проект, потребуєте допомоги у розвитку дитини або плануєте відкрити волонтерську 3D-ферму — вийдемо на зв'язок!", highlight_body_style)
    
    disclaimer_table = Table([[disclaimer_p1], [disclaimer_p2]], colWidths=[176*mm])
    disclaimer_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f9f9f9')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    disclaimer_table.hAlign = 'CENTER'
    story.append(disclaimer_table)
    story.append(Spacer(1, 4*mm))

    # Helper function to frame images tightly
    def make_boxed_image(path):
        img = Image(path, width=22*mm, height=22*mm)
        t = Table([[img]], colWidths=[24*mm], rowHeights=[24*mm])
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 1, colors.black),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    # 7. QR Section
    story.append(Paragraph("ПЕРЕГЛЯНУТИ МОЄ ПОВНЕ ПОРТФОЛІО ТА НАПИСАТИ:", qr_title_style))
    story.append(Spacer(1, 3*mm))

    qr1 = make_boxed_image("assets/qr_website.png")
    qr2 = make_boxed_image("assets/qr_organizer.png")

    qr_table_data = [
        [qr1, qr2],
        [
            Paragraph("САЙТ-ПОРТФОЛІО", qr_label_style),
            Paragraph("TELEGRAM ЗВ'ЯЗОК", qr_label_style)
        ],
        [
            Paragraph("Повний список проектів, коду, музики та контактів", qr_desc_style),
            Paragraph("Напишіть мені особисто: @robosapiens8", qr_desc_style)
        ]
    ]
    qr_table = Table(qr_table_data, colWidths=[88*mm, 88*mm])
    qr_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('BOTTOMPADDING', (0,1), (-1,1), 1),
        ('TOPPADDING', (0,1), (-1,-1), 3),
    ]))
    qr_table.hAlign = 'CENTER'
    story.append(qr_table)
    story.append(Spacer(1, 4*mm))

    # Separator line
    sep_table = Table([[""]], colWidths=[176*mm], rowHeights=[1])
    sep_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 1, colors.HexColor('#dddddd')),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(sep_table)
    story.append(Spacer(1, 3*mm))

    # 8. Footer
    footer_p = Paragraph("Тарас Москаленко · Людина. Творець. · Karlsruhe<br/><font size=6.5 color='#666666'>Impressum: Taras Moskalenko, Stresemannstraße 5, 76187 Karlsruhe | welcomeinkarlsruhe@gmail.com</font>", footer_style)
    story.append(footer_p)

    doc.build(story)
    print("Created taras_moskalenko_portfolio_a4.pdf")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    generate_qr_codes()
    create_html_poster()
    create_pdf_poster()
