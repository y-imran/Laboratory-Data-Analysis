from fpdf import FPDF


def add_text(
    pdf: FPDF,
    text: str,
    font_size: int = 10,
    bold: bool = False,
    color: tuple[int, int, int] = (60, 60, 60),
    align: str = "L",
    spacing_after: int = 5,
) -> None:
    """Add reusable text to the PDF.

    Parameters
    ----------
    pdf : FPDF
        PDF object.
    text : str
        Text to add.
    font_size : int, optional
        Font size (default is 10).
    bold : bool, optional
        Whether the text should be bold (default False).
    color : tuple, optional
        RGB text color (default (60, 60, 60)).
    align : str, optional
        Alignment: "L" = left, "C" = center, "R" = right (default "L").
    spacing_after : int, optional
        Space after the text block (default 5).
    """
    style = "B" if bold else ""
    pdf.set_font("Arial", style, font_size)
    pdf.set_text_color(*color)
    pdf.multi_cell(0, 6, text, align=align)
    pdf.ln(spacing_after)


class ReportPDF(FPDF):
    """Custom PDF class with predefined header and footer for the report."""

    def header(self) -> None:
        self.set_font(family="Arial", size=8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, "Laboratory Analytics Report", ln=True, align="R")
        self.ln(5)

    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def add_chart_section(pdf: FPDF, chart_path: str) -> None:
    """Add a chart image and placeholder for insight text to the PDF.

    Parameters
    ----------
    pdf : FPDF
        PDF object.
    chart_path : str
        Path to the chart image file.
    """
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(40, 40, 40)
    pdf.ln(5)
    # Chart image
    pdf.image(chart_path, x=20, w=170)
    pdf.ln(8)
    # Insight heading (placeholder styling – actual text added later via ``add_text``)
    pdf.set_font("Arial", "B", 11)
    pdf.set_text_color(40, 40, 40)
    pdf.ln(2)
    # Insight text styling – actual content added later via ``add_text``
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(70, 70, 70)
    pdf.ln(5)
