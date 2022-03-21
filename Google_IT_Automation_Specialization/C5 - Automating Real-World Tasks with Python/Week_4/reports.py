#!/usr/bin/env python3

# Using the reportlab Python library, define the method generate_report to build the PDF reports.

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.platypus import SimpleDocTemplate


# def generate_report(filename, title, additional_info, table_data):

#!/usr/bin/env python3


def generate_report(filename, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate()
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)

    report.build([report_title, empty_line, report_info])
