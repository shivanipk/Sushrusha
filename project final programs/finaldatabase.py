'''
Created on 11-Oct-2016

@author: Aishwarya-HP
'''
class Database:
    
    def con(self):
        import cx_Oracle
        scon =cx_Oracle.connect('aish/aish@127.0.0.1/xe')
        return scon
    
    def getId(self,scon,pname):
        
        cur=scon.cursor()
        np={'name':pname}
        stmt= 'select id from ptable where pname = :name'
        cur.execute(stmt,np)
        res = cur.fetchall()
        if not res:
            return 0
        else:
            tup=res[0]
            scon.commit()
            return tup[0]
        
            
    def getrcnt(self,scon,pid):
        cnt=0
        cur=scon.cursor()
        stmt= 'select rcnt from ptable where id = :id'
        cur.execute(stmt, {'id': pid})
        res = cur.fetchall()
        t=res[0]
        print(t[0])
        scon.commit()
        return t[0]
    
    def getpname(self,scon,pid):
        cur=scon.cursor()
        stmt= 'select pname from ptable where id = :id'
        cur.execute(stmt, {'id': pid})
        res = cur.fetchall()
        if not res:
            return ""
        else:
            tup=res[0]
            return tup[0]
    
    def getpath(self,scon,id):
        cur=scon.cursor()
        stmt='select rootlink from roottable where id=:pid'
        cur.execute(stmt,{'pid':id})
        res=cur.fetchall()
        t=res[0]
        return t[0]
    
    def updatecnt(self,scon,pid,cnt):
        cur=scon.cursor()
        stmt='update ptable set rcnt=:cnt where id=:id'
        cur.execute(stmt,{'id':pid,'cnt':cnt})
        scon.commit()
    
    def getIdcnt(self,scon):
        idcnt=0
        cur=scon.cursor()
        stmt= 'select idcnt from info where rno=1'
        cur.execute(stmt)
        for id1 in cur.fetchall():
            idcnt=id1[0]
        return idcnt
    
    def insertinfo(self,scon,cnt):
        cur=scon.cursor()
        stmt='update info set idcnt=:cnt where rno=1'
        cur.execute(stmt,{'cnt':cnt})
        scon.commit()
        
    
    def insertptable(self,scon,pid,pname,rcnt1):
        cur=scon.cursor()
        statement = 'insert into ptable(id,pname,rcnt) values (:1, :2, :3)'
        cur.execute(statement, (pid,pname,rcnt1))
        scon.commit()
        
    def insertlink(self,scon,pid,link,dt):
        cur=scon.cursor()
        statement = 'insert into linktable(id,link,rtime) values (:1, :2, :3)'
        cur.execute(statement, (pid,link,dt))
        scon.commit()
        
    def insertroot(self,scon,pid,rootl):
        cur=scon.cursor()
        statement = 'insert into roottable(id,rootlink) values (:1, :2)'
        cur.execute(statement, (pid,rootl))
        scon.commit()
    
            




