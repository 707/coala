from bears.tests.LocalBearTestHelper import verify_local_bear
from bears.natural_language.LanguageToolBear import LanguageToolBear


LanguageToolBear1Test = verify_local_bear(
    LanguageToolBear,
    valid_files=(["A correct English sentence sounds nice in everyone."],
                 ["Eine korrekte englische Satz klingt nett zu jedermann."]),
    invalid_files=(["  "],
                   ["asdgaasdfgahsadf"],
                   ['"quoted"']))


LanguageToolBear2Test = verify_local_bear(
    LanguageToolBear,
    valid_files=(["A correct English sentence sounds nice in everyone."],),
    invalid_files=(["Eine korrekte englische Satz klingt nett zu jedermann."],),
    settings={'locale': 'en-US'})
