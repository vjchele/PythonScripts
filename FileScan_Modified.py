import os
with open('files_with_errors.txt','w') as fe:
    with open('output.txt','w') as of:
        for r,d,f in os.walk("D:/Dli/CWDS/DEV-R12.2/WebRoot/CWDSOnline/"):
            for file in f:
                loc = os.path.join(r,file)
                if (".aspx.vb" in loc):
                        with open(loc) as fr:
                            try:
                                lines = fr.readlines()
                            except:
                                fe.write(loc + '\n')
                                continue
                            for line in lines:
                                ssr = line.strip()
                                if ssr.startswith('MyBase.SSRNumber') :
                                    of.write(loc +',' + ssr[ssr.find("=")+1:].strip() + '\n')
                                
                        

                       
           
                


