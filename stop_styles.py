import datetime
from openpyxl.styles import Border, Side, Alignment, Font

#  0  A  1   ITEM NUMBER          '@      l
#  1  B  2   ITEM NAME            '@      l
#  2  C  3   LOCATION             '@      l
#  3  D  4   PALLET ID            '@      l
#  4  E  5   AVAILABLE INV        '0      r
#  5  F  6   INV VALUE IN TOTAL   '$0.00  r

TODAY = datetime.date.today()

# column and row sizes
size_row = {'1': 30}
size_col = {'A': 21,
            'B': 36,
            'C': 11,
            'D': 12,
            'E': 12,
            'F': 12 }


def header_footer_options(ws, total=0):
    """header and footer styles and values."""
    ws.oddHeader.scaleWithDoc = False
    ws.oddHeader.left.text    = 'STOP REPORT'
    ws.oddHeader.left.font    = 'Iosevka Heavy'
    ws.oddHeader.left.size    = 24
    ws.oddHeader.center.text  = TODAY.strftime('%A / Week %U / {}'.format(TODAY.strftime('%Y%m%d')))
    ws.oddHeader.center.font  = 'Iosevka Medium'
    ws.oddHeader.center.size  = 10
    ws.oddHeader.right.text   = '${:.2f}'.format(total)
    ws.oddHeader.right.font   = 'Iosevka Medium'
    ws.oddHeader.right.size   = 16
    ws.oddFooter.center.text  = '&[Page] of &N'
    ws.oddFooter.center.font  = 'Iosevka'
    ws.oddFooter.center.size  = 9


def page_print_options(ws):
    """apply page and print options."""
    ws.page_margins.top    = 0.75
    ws.page_margins.bottom = 0.75
    ws.page_margins.left   = 0.3
    ws.page_margins.right  = 0.3
    ws.page_margins.header = 0.3
    ws.page_margins.footer = 0.3
    ws.page_setup.scale    = 96
    ws.print_title_rows    = '1:1'  # print col headers on every page
    ws.print_options.horizontalCentered = True  # center content to page, horizontal
    ws.title = TODAY.strftime('%Y%m%d')


def get_font(r, c):
    """get font options for cell address."""
    if r == 0: return Font(name='Iosevka', size=11, bold=True)
    else:      return Font(name='Iosevka', size=10)


def get_border(r,c):
    """get border options for cell address."""
    if r == 0: return Border(bottom=Side(border_style='thin', color='FF000000'))
    else:      return None


def get_alignment(r, c):
    """get cell alignment for cell address."""
    if   c in [0,1,2,3]: h = 'left'
    elif c in [4,5]:     h = 'right'
    wt = True if r == 0 else None
    return Alignment(horizontal=h, wrap_text=wt)


def get_number_format(r, c):
    """get number formate for cell address."""
    if   r == 0:         return '@'
    elif c in [0,1,2,3]: return '@'
    elif c in [4]:       return '0'
    elif c in [5]:       return '$0.00'


def apply_to_cell(cell, r, c):
    """apply all cell options for cell address."""
    cell.number_format = get_number_format(r, c)
    cell.alignment     = get_alignment(r, c)
    cell.border        = get_border(r, c)
    cell.font          = get_font(r, c)
