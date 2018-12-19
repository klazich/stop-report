import datetime
from openpyxl.styles import Border, Side, Alignment, Font

#  0  A  1  ITEM NUMBER              '@  l
#  1  B  2  INVENTORY MODEL GROUP    '@  c
#  2  C  3  SKIP LOT ID              '@  c
#  3  D  4  OVERRIDE INSPECTION      '@  c
#  4  E  5  MANUAL INSPECTION        '@  c
#  5  F  6  COUNTER STARTUP TRIGGER  '0  r
#  6  G  7  COUNTER TRIGGER          '0  r
#  7  H  8  COUNTER SKIPPED          '0  r

TODAY = datetime.date.today()

# column and row sizes
size_row = {'1': 45}
size_col = {'A': 30,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10,
            'F': 10,
            'G': 10,
            'H': 10 }


def header_footer_options(ws):
    """header and footer styles and values."""
    ws.oddHeader.scaleWithDoc = False
    ws.oddHeader.left.text    = 'MI REPORT'
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
    if   c in [0]:       h = 'left'
    elif c in [1,2,3,4]: h = 'center'
    elif c in [5,6,7]:   h = 'right'
    wt = True if r == 0 else None
    return Alignment(horizontal=h, wrap_text=wt)


def get_number_format(r, c):
    """get number formate for cell address."""
    if   r == 0:           return '@'
    elif c in [0,1,2,3,4]: return '@'
    elif c in [5,6,7]:     return '0'


def apply_to_cell(cell, r, c):
    """apply all cell options for cell address."""
    cell.number_format = get_number_format(r, c)
    cell.alignment     = get_alignment(r, c)
    cell.border        = get_border(r, c)
    cell.font          = get_font(r, c)
