class Mamagerdb:
    def selectdb(self,table):

@app.get(("/select/database)")
async def select_db(database,table):
     result = (database).selectdb(table)
     return {"select_data": result}