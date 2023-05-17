from collections import defaultdict


class Solution:

    def string_to_seq_start(self, s):
        shifts = ord(s[0]) - ord('a')
        seq = [''] * len(s)
        for i in range(len(s)):
            seq[i] = chr(((ord(s[i]) - shifts + 26) % 26) + ord('a'))
        return str(seq)

    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        table = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                table['a'].append(s)
            else:
                table[self.string_to_seq_start(s)].append(s)
        return list(table.values())


sol = Solution()
print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
print(sol.groupStrings(['a']))
print(sol.groupStrings(
    ["xzv", "tvhmtraayghfabutim", "scruzaydxrapcuv", "xiznzqqjbetchvhndzz", "qmbkbjpkxzmnwvo", "tttwsszaetyzgsaprv",
     "xdhbxxxomhagohdvdyv", "khugdmdbbqjbeuxq", "xzzqnowcyplkdxgkbbb", "daxzqsdcfuymlyevyfnayb",
     "nrlalrdjqqckogfqlhfhg", "akpellndulbbbipbvatbu", "pfqeu", "dneng", "rjnvgxk", "eujibxcxetdjztn", "aufkyfjuruaq",
     "izeqjoftsfzjkujiubkrb", "dwzuyrospzjzuckk", "kcuxsetkmzkq", "lvej", "lzefktml", "varaxwjxf",
     "cwdqxivcxeyzhsvqccy", "kzxlrqbabvtvkfajbjatzyix", "husuheaiirzowtiadgtxwf", "swtja", "ddvxhgesuenqdgutm", "uaduv",
     "t", "yvwfcproumulvnbva", "ddjikfsnasyj", "tqxiqlqkxbmwuytempvg", "yihridsxajkiyehmdbru", "pbxvdoleubrdd",
     "smavxt", "azlrmjwmlsglgwrdakgn", "cf", "ohkaajphvrorgyx", "nll", "jlnlqzviffdmegnxig", "pqgkqrancnwaqrjovjlgqsfx",
     "azwaipyqlmgoeslujdkwuh", "jubooimlfis", "sosnjvqikiivlighyktd", "jhujjiiovhw", "jgbj", "qtrbilvqvy",
     "vlmkkilhsqlknvqpus", "omuucd", "ligpithabxjqtuaf", "mz", "ognmihotoqgprvbt", "nmgwkocmeezb", "qmiajlowymr",
     "xmlmolj", "cwciqqpbmzzcgmnrvgucezor", "ng", "lqglykvsxhobqrppeqrlp", "ywuytvrproahtgro", "etcnjqg", "bogjahrw",
     "rrrkddajfq", "nwcraujocpk", "yo", "nhasjwodqyququhhfkyv", "tpalgbgirzrl", "jjgcsekxxi", "r", "jgxxttnlhez", "ha",
     "jxklqfdizkgzusrzs", "hnjctughrsdiyezcqsmij", "tvpawacxepvq", "lwv", "rspgmumnbrzk", "gqkdxbkylirxxqrhh", "wsbvir",
     "fjktj", "rulvjpezzonnbr", "kxntnopkkjgliltrlklfgc", "h", "uplapswlksu", "cevzkpfcbviliulexyx",
     "mvbwfqqbeisdsjdnn", "giavjwaftarskv", "trlhxmqayeiero", "yfazdiayalzrnf", "qmolgaezbwuodbdhsxclhzi", "nskgjmut",
     "gccpj", "psmqmdceprjoiw", "dhvqyqvnh", "jcxq", "quvi", "pvqdzzwv", "yzksz", "vnicvmnfwwwmzhsdsm", "gn",
     "jcyfpawtcnuikudwuijpd", "mmncorzbnoawyo", "cwygpjjmrmslabafcmwdhpdo", "nikwaflxpepnkz", "qmylnzkhz", "oc",
     "jnyibizgmwjqjvhbg", "ajhaejn", "eulboowdyd", "vyjfniqjoepdbzulvpgjic", "oauvt", "vpnmjbnkf", "izk", "sanouetznnk",
     "truufmplrmsxgvrtl", "yuabbnxybbpfgblou", "yjyawflsvetbdpcgbjta", "cmozvlftrhtxmjqkorxfrql",
     "nbyvnbhjlofqdtilvplcdks", "nxmyafxvrfhbuzpzixt", "lxtoignhwtcbsi", "cycu", "rlzjrirwfhwdvolixa", "itle", "nmitv",
     "cno", "mnwjytgktowostuzvrcjxr", "etus", "othjqfpysicbdhfezxpvhjd", "nzypfebzbsaakoky", "uimwaktcywogwptihvrrh",
     "pgc", "njwftpurketzvjbzivanz", "olnrizftjnjixeysi", "k", "fbwkolpka", "vqcxxbcumypdbetrknavgm",
     "ivfnyhqqnjdmdwqslhk", "fusfadhqfruriiglvqzuns", "r", "sghqrdaelollqmczagojceys"]))
