from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image,
                                Table, TableStyle, KeepTogether, HRFlowable)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'report' / 'Capstone_Report.pdf'
DIMG = ROOT / 'diagrams' / 'network_diagram.png'
SCREENSHOT = ROOT / 'evidence' / 'initial_dvwa_home_screenshot_context.png'

NAVY = colors.HexColor('#142844')
BLUE = colors.HexColor('#245B88')
TEAL = colors.HexColor('#168C87')
PALE = colors.HexColor('#EFF5FA')
MUTED = colors.HexColor('#56657A')
BORDER = colors.HexColor('#CCD7E2')
ORANGE = colors.HexColor('#B87517')
RED = colors.HexColor('#A83F48')

# Register available DejaVu fonts for reliable PDF rendering.
font_regular = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font_bold = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if Path(font_regular).exists() and Path(font_bold).exists():
    pdfmetrics.registerFont(TTFont('DV', font_regular))
    pdfmetrics.registerFont(TTFont('DV-Bold', font_bold))
    BASE='DV'; BOLD='DV-Bold'
else:
    BASE='Helvetica'; BOLD='Helvetica-Bold'

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverLabel', fontName=BOLD, fontSize=10, leading=14, textColor=TEAL, tracking=1.2, spaceAfter=9))
styles.add(ParagraphStyle(name='CoverTitle', fontName=BOLD, fontSize=28, leading=34, textColor=NAVY, spaceAfter=15))
styles.add(ParagraphStyle(name='CoverSubtitle', fontName=BASE, fontSize=13, leading=19, textColor=MUTED, spaceAfter=10))
styles.add(ParagraphStyle(name='H1x', fontName=BOLD, fontSize=19, leading=24, textColor=NAVY, spaceBefore=4, spaceAfter=10, keepWithNext=True))
styles.add(ParagraphStyle(name='H2x', fontName=BOLD, fontSize=12, leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name='Bodyx', fontName=BASE, fontSize=9.2, leading=14, textColor=colors.HexColor('#25354A'), spaceAfter=7))
styles.add(ParagraphStyle(name='Smallx', fontName=BASE, fontSize=8, leading=11, textColor=MUTED, spaceAfter=4))
styles.add(ParagraphStyle(name='Tinyx', fontName=BASE, fontSize=7, leading=9, textColor=MUTED))
styles.add(ParagraphStyle(name='Callout', fontName=BASE, fontSize=9, leading=13, textColor=NAVY, backColor=PALE, borderColor=BORDER, borderWidth=0.7, borderPadding=8, spaceBefore=5, spaceAfter=10))
styles.add(ParagraphStyle(name='Codex', fontName='Courier', fontSize=8.2, leading=11.5, textColor=colors.HexColor('#20324C'), backColor=PALE, borderColor=BORDER, borderWidth=0.5, borderPadding=7, leftIndent=4, rightIndent=4, spaceBefore=4, spaceAfter=8))
styles.add(ParagraphStyle(name='Cell', fontName=BASE, fontSize=7.6, leading=10, textColor=colors.HexColor('#25354A')))
styles.add(ParagraphStyle(name='CellBold', fontName=BOLD, fontSize=7.6, leading=10, textColor=NAVY))
styles.add(ParagraphStyle(name='CenterSmall', fontName=BASE, fontSize=8, leading=11, textColor=MUTED, alignment=TA_CENTER))


def P(text, style='Bodyx'):
    return Paragraph(text, styles[style])

def bullet(text):
    return Paragraph('&bull;&nbsp;&nbsp;' + text, styles['Bodyx'])

def tbl(data, widths, header=True):
    t=Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    ts=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('GRID',(0,0),(-1,-1),0.45,BORDER)]
    if header:
        ts += [('BACKGROUND',(0,0),(-1,0),NAVY),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),BOLD)]
        for i in range(len(data[0])):
            if isinstance(data[0][i], str):
                data[0][i]=Paragraph(data[0][i], ParagraphStyle('th'+str(i), fontName=BOLD,fontSize=7.8,leading=10,textColor=colors.white))
    for r in range(1 if header else 0,len(data)):
        if r%2==0: ts.append(('BACKGROUND',(0,r),(-1,r),colors.HexColor('#F7F9FC')))
    t.setStyle(TableStyle(ts))
    return t

def footer(canvas, doc):
    canvas.saveState()
    w,h=A4
    if doc.page>1:
        canvas.setStrokeColor(BORDER); canvas.setLineWidth(.6)
        canvas.line(18*mm,h-15*mm,w-18*mm,h-15*mm)
        canvas.setFont(BOLD,7.5); canvas.setFillColor(NAVY)
        canvas.drawString(18*mm,h-11.5*mm,'DVWA SQLi CAPSTONE')
        canvas.setFont(BASE,7.5); canvas.setFillColor(MUTED)
        canvas.drawRightString(w-18*mm,h-11.5*mm,'Draft template - replace placeholders with actual evidence')
    canvas.setStrokeColor(BORDER); canvas.setLineWidth(.6)
    canvas.line(18*mm,14*mm,w-18*mm,14*mm)
    canvas.setFont(BASE,7.5); canvas.setFillColor(MUTED)
    canvas.drawString(18*mm,9*mm,'Controlled local lab only | No production system was tested by this template')
    canvas.drawRightString(w-18*mm,9*mm,f'Page {doc.page}')
    canvas.restoreState()

story=[]
# Cover
story += [Spacer(1,18*mm), P('CAPSTONE PROJECT | WEB APPLICATION SECURITY','CoverLabel'),
          P('Web Application Penetration Testing<br/>and Incident Response Using DVWA','CoverTitle'),
          P('A practical, evidence-driven SQL injection assessment in a controlled training environment','CoverSubtitle'),
          Spacer(1,7*mm), HRFlowable(width='100%', thickness=2.2, color=TEAL, spaceBefore=4, spaceAfter=17),
          P('<b>Prepared by:</b> [FILL IN NAME]','Bodyx'),
          P('<b>Program / internship:</b> [FILL IN]','Bodyx'),
          P('<b>Assessment date:</b> [FILL IN]','Bodyx'),
          P('<b>Target:</b> DVWA local lab at [VERIFY URL]','Bodyx'),
          Spacer(1,10*mm),
          P("<b>IMPORTANT - DRAFT TEMPLATE.</b> This is not a completed penetration-test result. Actual SQLi behavior, screenshots, logs, and response outcomes must be added from the user's own lab. No vulnerability is claimed as confirmed in this document.",'Callout'),
          Spacer(1,15*mm), P('Primary deliverables','H2x'),
          P('Report PDF  |  GitHub-ready repository  |  Network diagram  |  Evidence register  |  Offline log detector  |  12-minute video script','Bodyx'),
          Spacer(1,7*mm), P('Method reference: OWASP Web Security Testing Guide and SQL Injection Prevention Cheat Sheet','Smallx'), PageBreak()]

# Executive Summary & plan
story += [P('1. Executive Summary','H1x'),
          P('This capstone is designed to test a deliberately vulnerable DVWA instance, document a controlled SQL injection experiment, and simulate basic incident detection and response using local web logs. It emphasizes scope control, observable evidence, practical mitigations, and honest reporting.'),
          P('<b>Current report status:</b> Draft / evidence pending. The supplied browser screenshot shows the DVWA home page at a loopback URL, but it does not establish that a SQL injection test was performed. Replace the placeholders below only after testing.','Callout'),
          tbl([[P('Field','CellBold'),P('Value','CellBold')],
               [P('Actual SQLi result','Cell'),P('[CONFIRMED / NOT CONFIRMED / INCONCLUSIVE - fill after test]','Cell')],
               [P('Target URL','Cell'),P('[Verify current live endpoint, e.g. http://127.0.0.1:4280]','Cell')],
               [P('Security setting','Cell'),P('[Record selected DVWA security level]','Cell')],
               [P('Evidence','Cell'),P('[E01-E06 filenames in evidence register]','Cell')],
               [P('Retest status','Cell'),P('[Not performed / performed with results]','Cell')]], [45*mm,124*mm]),
          P('2. Objectives and Scope','H1x'),
          P('Objectives','H2x'), bullet('Establish normal baseline behavior of the DVWA SQL Injection module.'),
          bullet('Use a limited input-validation and Boolean-condition test in the local training target.'),
          bullet('Record screenshots and sanitized HTTP/log evidence, then explain actual results.'),
          bullet('Recommend secure query handling and demonstrate basic log triage/incident response.'),
          P('Scope','H2x'), bullet('In scope: the project owner\'s local DVWA instance, initial security level Low, and logs generated by the controlled test.'),
          bullet('Out of scope: public sites, unrelated systems, destructive changes, denial of service, credential/hash dumping, and real user data.'),
          P('Authorization and safety','H2x'),
          P('All testing is limited to a deliberately vulnerable local lab. Keep DVWA bound to loopback or an isolated lab network. Do not place the app on a public interface. Save only sanitized evidence.'), PageBreak()]

# Environment and diagram
story += [P('3. Environment and Architecture','H1x'),
          P('Record the real environment below. Do not assume that a browser tab or cached page means the service is currently running.'),
          tbl([[P('Item','CellBold'),P('Value to record','CellBold')],
               [P('Kali VM / OS','Cell'),P('[Distribution and version]','Cell')],
               [P('DVWA version / image','Cell'),P('[FILL IN]','Cell')],
               [P('URL and port','Cell'),P('[Verify live URL]','Cell')],
               [P('Runtime','Cell'),P('[Docker Compose / other]','Cell')],
               [P('Log source','Cell'),P('[Apache access log / container logs / other]','Cell')]], [46*mm,123*mm]),
          Spacer(1,5*mm), Image(str(DIMG), width=169*mm, height=95.8*mm),
          P('Figure 1. Intended local architecture. Confirm actual interfaces and ports during setup; the diagram is a plan, not a discovery result.','Smallx'),
          P('Initial application screenshot','H2x')]
if SCREENSHOT.exists():
    img=Image(str(SCREENSHOT))
    img.drawWidth=169*mm; img.drawHeight=img.imageHeight*(169*mm/img.imageWidth)
    story += [img, P('Figure 2. User-provided DVWA home page screenshot with a loopback URL. It is setup evidence only and does not demonstrate a SQLi result.','Smallx')]
else:
    story += [P('[Insert screenshot E01 showing the live DVWA page and verified local URL.]','Callout')]
story += [PageBreak()]

# Methodology
story += [P('4. Methodology and Controlled Test Procedure','H1x'),
          P('Use a repeatable sequence: confirm scope and isolation, verify only the local DVWA port with curl/Nmap, capture a normal baseline, make one controlled input change at a time, compare responses, preserve evidence, and stop after the demonstrated effect.'),
          tbl([[P('Step','CellBold'),P('Action','CellBold'),P('Evidence','CellBold')],
               [P('1. Recon / scan','Cell'),P('Verify only 127.0.0.1:4280 using curl and a narrow Nmap service check; record the actual output.','Cell'),P('E01','Cell')],
               [P('2. Baseline','Cell'),P('Open SQL Injection; submit `1`; record the normal output.','Cell'),P('E02','Cell')],
               [P('3. Syntax probe','Cell'),P('Submit `1\'`; record error, rejection, or normal response exactly.','Cell'),P('E03','Cell')],
               [P('4. Boolean comparison','Cell'),P('Compare `1\' OR \'1\'=\'1` with `1\' AND \'1\'=\'2`.','Cell'),P('E04','Cell')],
               [P('5. Log review','Cell'),P('Inspect local web logs around the test time and run the offline indicator scanner.','Cell'),P('E05','Cell')],
               [P('6. Retest','Cell'),P('Record mitigation advice and retest only if a fix was actually applied.','Cell'),P('E06','Cell')]], [33*mm,105*mm,31*mm]),
          P('Important difference between the supplied tutorial and this project','H2x'),
          P('The supplied video transcript discusses bWAPP\'s search input and GET parameter. This project uses DVWA, where the standard SQL Injection module is commonly a User ID input. Do not copy bWAPP parameter names or assume that its selected-column count matches DVWA.'),
          P('Controlled SQLi input examples','H2x'),
          P('<b>Baseline:</b> <font name="Courier">1</font><br/><b>Quote probe:</b> <font name="Courier">1\'</font><br/><b>True condition:</b> <font name="Courier">1\' OR \'1\'=\'1</font><br/><b>False condition:</b> <font name="Courier">1\' AND \'1\'=\'2</font>','Codex'),
          P('Use these only in your own DVWA instance. Compare what your page actually shows. Do not dump password hashes, enumerate unrelated tables, alter records, or run destructive queries.' ,'Callout'),
          P('What counts as evidence','H2x'),
          bullet('A baseline screenshot and the exact security level.'),
          bullet('A screenshot of the quote probe response; do not infer more than it supports.'),
          bullet('A paired true/false response screenshot or equivalent Burp request/response with cookies redacted.'),
          bullet('The timestamp and a relevant, sanitized log line if available.'), PageBreak()]

# Finding template
story += [P('5. Finding and Mitigations','H1x'), P('Finding F-01: SQL Injection test in DVWA'),
          tbl([[P('Attribute','CellBold'),P('Entry','CellBold')],
               [P('Status','Cell'),P('[CONFIRMED / NOT CONFIRMED / INCONCLUSIVE]','Cell')],
               [P('Affected module/parameter','Cell'),P('[FILL IN from the actual request]','Cell')],
               [P('Severity','Cell'),P('[Rate with a rationale based on observed impact and context]','Cell')],
               [P('Evidence IDs','Cell'),P('[E02, E03, E04; add actual file paths]','Cell')],
               [P('Finding summary','Cell'),P('[Describe baseline versus test responses without exaggeration]','Cell')]], [48*mm,121*mm]),
          P('Technical explanation','H2x'),
          P('SQL injection may occur when user-controlled input is concatenated into SQL syntax instead of being bound as data. The impact depends on the query, privileges, database configuration, and reachable data. Report only effects observed in this lab and separate them from theoretical worst-case impact.'),
          P('Recommended mitigations','H2x'),
          bullet('Use parameterized queries / prepared statements; do not build SQL by concatenating input.'),
          bullet('Apply allow-list validation when the field is expected to be a known identifier or other restricted value.'),
          bullet('Use a database account with the minimum permissions required by the application.'),
          bullet('Return generic client-facing errors; keep detailed diagnostics in restricted server logs.'),
          bullet('Add regression tests for normal, invalid, and SQL-metacharacter inputs.'),
          bullet('Monitor suspicious request patterns; treat pattern matches as triage signals, not proof by themselves.'),
          P('Retest and status','H2x'),
          P('[If source code was not modified and the fix retested, say: "Mitigations recommended; application-level fix not applied or verified in this exercise." Do not call the finding remediated without evidence.]','Callout'),
          P('Severity guidance','H2x'),
          P('For this intentionally vulnerable training application, severity is a learning assessment. If confirmed, justify the rating using demonstrated data exposure or query manipulation, required access, and likely impact in a hypothetical production context. Do not call a finding Critical merely because the module is designed to be vulnerable.'), PageBreak()]

# Incident response
story += [P('6. Incident Detection and Response Simulation','H1x'),
          P('Scenario: a controlled SQLi-like request is sent to local DVWA during the test window. The analyst reviews local logs, identifies the request, documents containment, and records remediation/retest status.'),
          P('Detection script','H2x'),
          P('The included `scripts/detect_sqli_logs.py` reads a local text file and flags a small set of suspicious SQL-related strings. It is offline: it does not generate requests. Results are heuristic and may include false positives and false negatives.'),
          P('Example command','H2x'), P('python3 scripts/detect_sqli_logs.py evidence/actual_access.log','Codex'),
          P('The included `scripts/sample_access.log` is synthetic. If you use it to demo the detector, state on the video and in the report that it is synthetic, not output from your target.' ,'Callout'),
          tbl([[P('Response phase','CellBold'),P('Required action','CellBold'),P('Record','CellBold')],
               [P('Detect','Cell'),P('Flag suspicious request pattern and timestamp.','Cell'),P('[log source / output]','Cell')],
               [P('Triage','Cell'),P('Correlate with the controlled test time and browser evidence.','Cell'),P('[request / EIDs]','Cell')],
               [P('Contain','Cell'),P('For this disposable lab, stop DVWA after preserving evidence or restrict local access.','Cell'),P('[action + time]','Cell')],
               [P('Eradicate / remediate','Cell'),P('Document prepared statements and least privilege; apply and verify only if in scope.','Cell'),P('[change/retest]','Cell')],
               [P('Recover','Cell'),P('Verify the expected service state and retest safely if a fix was made.','Cell'),P('[result]','Cell')],
               [P('Lessons learned','Cell'),P('Improve query handling, error handling, logging, monitoring, and regression testing.','Cell'),P('[summary]','Cell')]], [34*mm,99*mm,36*mm]),
          P('Post-incident summary to complete','H2x'),
          P('Incident ID: IR-01<br/>Start/end time: [FILL IN]<br/>Detection source: [FILL IN]<br/>Indicator: [FILL IN]<br/>Containment performed: [FILL IN]<br/>Remediation/retest result: [FILL IN]<br/>Residual limitations: [FILL IN]','Bodyx'), PageBreak()]

# Deliverables and evidence
story += [P('7. Deliverables and Evidence Checklist','H1x'),
          tbl([[P('Deliverable','CellBold'),P('Contents','CellBold'),P('Status','CellBold')],
               [P('PDF report','Cell'),P('Executive summary, scope, methodology, findings, mitigations, incident response, references, actual screenshots.','Cell'),P('Template - update','Cell')],
               [P('GitHub repository','Cell'),P('README, checklist, diagram, script, evidence register, report source.','Cell'),P('Starter kit','Cell')],
               [P('12-minute video','Cell'),P('Live walkthrough plus actual outputs and honest limitations.','Cell'),P('Script included','Cell')],
               [P('Final link list','Cell'),P('Public/private repo URL, hosted report URL, video URL.','Cell'),P('Fill after publishing','Cell')]], [36*mm,103*mm,30*mm]),
          P('Evidence register (minimum set)','H2x'),
          tbl([[P('ID','CellBold'),P('Filename','CellBold'),P('Purpose','CellBold')],
               [P('E01','Cell'),P('E01_dvwa_home.png','Cell'),P('Live DVWA URL and environment','Cell')],
               [P('E02','Cell'),P('E02_sqli_baseline.png','Cell'),P('Normal request/response','Cell')],
               [P('E03','Cell'),P('E03_sqli_quote_test.png','Cell'),P('Controlled quote test','Cell')],
               [P('E04','Cell'),P('E04_sqli_boolean_test.png','Cell'),P('True/false comparison','Cell')],
               [P('E05','Cell'),P('E05_access_log_detection.png','Cell'),P('Log source and detector output','Cell')],
               [P('E06','Cell'),P('E06_remediation_retest.png','Cell'),P('Retest; if no fix applied, show mitigation plan instead','Cell')]], [16*mm,57*mm,96*mm]),
          P('Submission QA','H2x'),
          bullet('Replace every `[FILL IN]` marker; remove this warning only after evidence is complete.'),
          bullet('Make sure the finding status is supported by the screenshots and observed responses.'),
          bullet('Label the synthetic log sample as synthetic if used.'),
          bullet('Redact cookies, session IDs, tokens, and private personal data.'),
          bullet('Open the final PDF and play the video before sharing links.'), PageBreak()]

# Resources
story += [P('8. References and Learning Links','H1x'),
          P('Learning videos','H2x'),
          P('1. bWAPP SQL injection tutorial supplied for background: https://www.youtube.com/watch?v=ZaLWQ89b5f8<br/>2. DVWA SQL Injection (low/medium/high/impossible) walkthrough: https://www.youtube.com/watch?v=5bj1pFmyyBA<br/>3. SQL Injection for Beginners (DVWA walkthrough): https://www.youtube.com/watch?v=aYFZp80eOb0','Bodyx'),
          P('Note: the first video transcript is about bWAPP and its search parameter. The lab here uses DVWA; test the DVWA field and request as it actually behaves. Do not claim you performed a bWAPP test.','Callout'),
          P('Authoritative references','H2x'),
          P('1. OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/<br/>2. OWASP SQL Injection testing guide: https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Injection/05-SQL_Injection/<br/>3. OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html<br/>4. Official DVWA repository: https://github.com/digininja/DVWA','Bodyx'),
          Spacer(1,10*mm), HRFlowable(width='100%', thickness=1.5, color=TEAL, spaceBefore=5, spaceAfter=12),
          P('Final note','H2x'),
          P('This PDF is a professionally structured starter report, not a fabricated completed assessment. The actual test outcome and screenshots must come from the local DVWA run. Update the report and regenerate the PDF before final submission.'),
          Spacer(1,10*mm), P('Report template ends here','CenterSmall')]

doc=SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=22*mm, bottomMargin=19*mm,
                      title='DVWA SQLi Capstone Report - Draft Template', author='Capstone Starter Kit')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
