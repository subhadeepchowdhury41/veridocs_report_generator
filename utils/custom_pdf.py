from fpdf import FPDF, enums, XPos, YPos

class PDF(FPDF):
    height_covered = 0
    prev_top = 0
    row_height = 0
    height_covered = 0
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        super().set_font('helvetica', '', 14)
        super().set_auto_page_break(auto=True, margin=27)
        super().set_top_margin(30)
        super().add_page()
        self.line_height = super().font_size_pt*1.5

    def header(self):
        super().cell(w=10, txt="Hello")
        return super().header()

    def calc_required_rows(self, key, value):
        no_of_lines = (len(key) / 10).__ceil__()
        print(no_of_lines)
        return no_of_lines
    
    def create_pdf(self, form, response):
        for page in form['data']:
            page_no = page['id']
            for field in page['fields']:
                prev_top=self.y
                field_no = field['id']
                self.row_height = self.font_size_pt*self.calc_required_rows(field['label'], '')
                self.multi_cell(w=40, txt=field['label'],
                 align=enums.Align.C, new_x=XPos.RIGHT, new_y=YPos.TOP)
                if f'{page_no},{field_no}' in response:
                    res = str(response[f'{page_no},{field_no}'])
                    self.multi_cell(w=150, h=self.row_height, align=enums.Align.C, txt=res, new_x=XPos.RIGHT, new_y=YPos.TOP)
                else:
                    self.multi_cell(w=150, txt="", h=self.row_height,
                     new_x=XPos.RIGHT, align=enums.Align.C, new_y=YPos.TOP)
                
                self.ln(self.row_height)

                self.set_line_width(0.3)
                self.set_draw_color(0, 0, 0)

                prev_top -= 5

                self.line(x1=10, y1=prev_top, x2=200, y2=prev_top)
                self.line(x1=10, y1=prev_top+self.row_height, x2=200,
                 y2=prev_top+self.row_height)
                
                self.line(x1=10, y1=prev_top, x2=10, y2=prev_top+self.row_height)
                self.line(x1=50, y1=prev_top, x2=50, y2=prev_top+self.row_height)
                self.line(x1=200, y1=prev_top, x2=200, y2=prev_top+self.row_height)
                self.height_covered += self.row_height
                if self.height_covered >= 230:
                    self.height_covered = 0
                    super().add_page()
