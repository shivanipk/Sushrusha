'''
Created on 25-Oct-2016

@author: Aishwarya-HP
'''



class MainSpeech:
    
    def mainspeech(self):
        
        sfinal="empty"
        import os
        #from ai.file import time1
        #t=time1()
        from ai.finaldatabase import Database
        dobj=Database()
        fcon=dobj.con()
        rootpath="F:\\speechDB"

        prootpath=os.path.join("F:\\speechDB","patient")
        filerootpath=""
        from ai.tmpspeech import tmpspeech
        from ai.liver import liver
        from ai.Paragraph import Paragraph
        l=liver() 
        p=Paragraph()
        while(sfinal!="finish"):
            print('......listening.................')
    
           
            print("say something:")
    
            obj=tmpspeech()
            sfinal=obj.speech()
            print(sfinal)
            
            
            
            if(sfinal=='new'):
                print("in new")
                reportcnt=1
                while(1):
                    
                    print("tell patient name")
                    obj1=tmpspeech()
                    pname=obj1.speech()
                    if(len(pname)==0 or len(pname)>40):
                        continue
                    else:
                        break
                        
                
                print(pname)
                
                prootpath=os.path.join("F:\\speechDB","patient")
                idcnt=dobj.getIdcnt(fcon)
                tmpcnt=str(idcnt)
                prootpath=prootpath+str(idcnt)
                if not os.path.exists(prootpath):
                    os.makedirs(prootpath)
                filerootpath=prootpath+'\\'+pname+str(reportcnt)+'.docx'
                dobj.insertptable(fcon,idcnt,pname,reportcnt)
                dobj.insertlink(fcon,idcnt,filerootpath,"")
                dobj.insertroot(fcon,idcnt,prootpath)
                print(filerootpath)
                idcnt=idcnt+1
                dobj.insertinfo(fcon,idcnt)
                l.createf(filerootpath)
                l.filecopy(filerootpath)
                l.p1(filerootpath,pname)
                l.id2(filerootpath,tmpcnt)
            if(sfinal=='update'):
                print("in update")
                
                while(1):
                    print("tell patient id")
                    obj1=tmpspeech()
                    id1=obj1.speech()
                    print(id1)
                    if(len(id1)==0 or any(c.isalpha() for c in id1)):
                        continue
                    else:
                        pid=int(id1)
                        pname=dobj.getpname(fcon,pid)
                        if(len(pname)==0):
                            print("incorrect id")
                            continue
                        else:
                            break
                    
               
                
                print(pname)
        
                prootpath=dobj.getpath(fcon,pid)
                prcnt=dobj.getrcnt(fcon,pid)
                prcnt=prcnt+1
                dobj.updatecnt(fcon,pid,prcnt)
                filerootpath=prootpath+'\\'+pname+str(prcnt)+'.docx'
                print(filerootpath)
                dobj.insertlink(fcon,pid,filerootpath,"")
                l.createf(filerootpath)
                l.filecopy(filerootpath)
                l.id2(filerootpath,id1)
                l.p1(filerootpath,pname)
                
            
            if(sfinal=='paragraph'):
                print("in paragraph")
                print("tell paragraph name that you want to include or copy normal para")
                obj2=tmpspeech()
                pstr=str(obj2.speech())
                print(pstr)
                if(pstr=='liver'):
                    print("liver para added")
                    p.liverP(filerootpath)
                if(pstr=='gallbladder'):
                    print("gall badder para added")
                    p.gallbladder(filerootpath)
                if(pstr=='kidney'):
                    print("kidney para added")
                    p.kidney(filerootpath)
                
                
            if(sfinal=='general'):
                print("in general")
                p.general(filerootpath)           
            
            if(sfinal=='kidney parameter'):
                print("for left kidney tell size")
                l.k1(filerootpath)
                print("for right kidney tell size")
                l.k2(filerootpath)   
                #print("tell stone present or not") 
                l.stone(filerootpath)
                l.hyper(filerootpath)
            
            if(sfinal=="liver parameter"):
                print(" does liver contours appear normal or abnormal? ")
                l.l5(filerootpath)
                print("Is Focal mass lesion present or absent?")
                l.l1(filerootpath)
                print("Does The portal vein and C.B.D appear normal or abnormal?")
                l.l2(filerootpath)
                print("Is liver is fatty or not say yes or no")
                l.l3(filerootpath)
                print("Does hepatic portal and venous system appear normal or abnormal?")
                l.l4(filerootpath)
                
            if(sfinal=="display"):
                print("in display")
                l.display(filerootpath)
        
        
    



obj=MainSpeech()
obj.mainspeech()

       
    
