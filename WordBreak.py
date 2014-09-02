__author__ = 'butterfly'

#s[0..k],s[k+1..n]
#s[0..j]


class Solution:
    def inDict(self,s,dict):
        return s in dict
       # for ele in dict:
            #element = str(ele)
            #element.
        #    if ele == s:
         #       return True
        #return False

    def match(self,s,start,length,dict,set,depth):
        if length == 0:
            first = True
            result = ""
            for ele in set:
                if first == False:
                    result = result + " "
                result = result + ele
            self.wordsList.append(result)
            self.result = True
            return True
        if self.result == True:
            return True
        #if self.result:
         #   return True
        #size = length
        #self.depth = self.depth + 1
        #if self.depth > 20:
         #   return False
        #print(s[start:start+length])
        if self.predict(s[start:start+length],dict) == False:
            return False
        for element in dict:
            #size =length - i
            if len(element) > length:
                continue
            if s.startswith(element,start,start+length) == False:
                continue
           # print(substr)
           # if self.inDict(substr,dict):
               # print("word is:%s,size is:%d"%(substr,length-size))
            set.append(element)
            flag = self.match(s,start+len(element),length-len(element),dict,set,depth+1)
             #   if flag:
              #      return True
            set.pop(depth)
            if self.result:
                return True
           # size = size - 1

        return False
    def predict(self,s,dict):
        for char in s:
            flag = False
            for ele in dict:
               # print("char is:%s,Element is:%s"%(char,ele))
                if char in ele:
                    flag = True
                    break
            if flag == False:
                #print("%s%s"%(char,dict))
                return False
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        self.depth = -1
      #  print(len(s))
        self.result = False
        self.length = []
        for element in dict:
            self.length.append(len(element))
        self.length.sort()
        self.length.reverse()
       # dict.sort()
        #dict.reverse()
       # print(self.length)
       # if self.predict(s,dict) ==  False:
        #    return False
        self.wordsList = []
        self.match(s,0,len(s),dict,[],0)
        return self.result
print(Solution().wordBreak("a",["a"]))
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(Solution().wordBreak("cofjdnfdnjbejdhbkhechoeindgmkeloaibeffoacbieekebbfimhdehmncdcajhknidl", ["khjhhagijlickgjob","ajhknidl","khech","kjigndmcl","mbmodglgbahcmdcdoea","lnllaflae","enhakibofef","gjhegnfhlibiog","ajlfkmccbahbbggn","inbanhdomnnghdj","ghigcndibhmeojchbbogkgb","cdebhjjifcnmmmccoj","majcemhhdg","ccfhclceoh","ljfjlaghjehk","mljn","anifljijkdhociken","fogabkbbd","cjahcbienajcgakjjig","kkfffg","jchelakgio","mkkaklj","obehecobkolile","eejne","ndoeic","fbfnkehm","e","mam","hdbibbfijcnlomabemombog","lo","egbklbihgangemjb","jmckjbkbodfknffbchfgie","hldlkfclidhfalmlonfj","diabnkcbadjfmncenihfhk","lamnnbhbaak","cgjmekgfkogclha","nifaifhkbl","eimgallmelmi","mchglmn","fladoo","admmdklfogkafedhnkikell","nfceebenebjgffillm","bacnnmhilkfkffflhdjkhb","fdmbgmckefhenhn","cofjdnfdnjbej","lcmooada","iikimdf","aoloadmajamljdcbfeo","jhoebchekagjlellllm","dh","agk","nlgb","ldihehjafnkcakofebgloam","cbgkafkljdaea","jillnbnglddhdjaf","bjnhobhaalaanijcblhfjfj","difdoaj","mfmcgmaekia","dofkioedciimljhdeehd","kegnobengjbbiko","aamlocelnmib","oeemgcnfamlmdljfdmflfjj","eff","klblolckacndmangjm","kieec","ldljcjchn","blbeg","minibhaoegameolbchfdmd","aahofmcngcdle","lgihd","mmmkj","eoajcgncdafj","ehgkknkefkgkmfbnkfgn","jnniindkohgjdnbjj","mjgkooiklknbnohbn","cddhoglffhikhf","hkojnkclkfjdkno","bhamagfa","cclfechbhkkbikjnfiam","caihcen","ddo","cndgo","mmecggd","k","cnccdoiflnincgacakdoffkdg","eadblmgaioccedaabjfli","jielegjn","kmcnckacoifjamh","ljladkigjjcklnfjagdbbm","na","nblkbmcmmlible","aobkbkeljbhm","jinalibnjhghkdegejfkhojmb","eahacl","chefiggjndcnmlhfelbffea","nbekmjcgjhbnm","hkgabejjogecnlnollhdmc","kc","lhifcackehclg","c","fcna","docgijgankik","b","kfmnoenngjhbkjdbbdb","fmajfjg","imaalcbeibmondaen","loaibeffoacbieekebhmncdc","mchdeedmhmimjeg","oebgcilngjfalebeonbgjmhb","igaieibkhklncikm","lkmhimcj","ahfehlfbimgbgc","hemaimhfnigmfnabco","l","jahkbcdonia","i","bfimhde","ciekchnoolgkjnijekjehcagl","iob","gjldfmnaldnclofg","bbghhfbmknflddiabgj","gholddmbmnhii","iodn","cckkmijgcdjkglfd","njmdahlgbloimibfdco","cjdekg","oeindgmke","mbdcgebgdk","jlddkmoe","oegbiannddkmhibjokkm","loaejecbcondlgaeenbjlokjg","dlchahdimcdjobkfoce","haamgab","fkbj","aggodojjglicnf","gahadoafofdbeieihklfg","aembllfaiggee","ljnjfhknfjf","lhkobdkmnkmaf","ilgcde","nghclbilaiombcidj","igamidcjibblokkmjkhnha","ceiikahhicgbdlhlo","hdcfnig","fbbignkajdjgn","ogjkbcccdldmea","ihnoenlokk","blk","aifhjmimhnggogajflkgc","jfoiif"]
))