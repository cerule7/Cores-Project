from enum import Enum


# Keeping all of the cores in one place will make them easier to use than passing around strings all the time.
# We can access all of them as set(Core), or a specific one as Core.wc, etc.
class Core(Enum):

    wc = 'WC'
    wcr = 'WCr'
    wcd = 'WCd'
    ns = 'NS'
    ns2 = 'NS2'
    scl = 'SCL'
    hst = 'HST'
    qq = 'QQ'
    qr = 'QR'
    itr = 'ITR'
    cc = 'CC'
    cc2 = 'CC2'
    ahp = 'AHp'
    ahq = 'AHq'
    aho = 'AHo'
    ahr = 'AHr'

    @property
    def code(self):
        return self.value
