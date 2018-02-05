from enum import Enum


# Keeping all of the cores in one place will make them easier to use than passing around strings all the time.
# We can access all of them as set(Core), or a specific one as Core.wc, etc.
class Core(Enum):

    wc = 'WC'
    wcr = 'WCr'
    wcd = 'WCd'
    ns = 'NS'
    scl = 'SCL'
    hst = 'HST'
    qq = 'QQ'
    qr = 'QR'
    itr = 'ITR'
    cc = 'CC'
    ahp = 'Ahp'
    ahq = 'Ahq'
    aho = 'Aho'
    ahr = 'Ahr'
