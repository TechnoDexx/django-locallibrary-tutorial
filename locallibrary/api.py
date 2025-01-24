from ninja import NinjaAPI
api=NinjaAPI()

@api.get("/")
async def index(request):
  return {"message":"Hello World"}
@api.get("/hello")
async def Hello(request,name="World"):
  return {"message":f"Hello {name}"}
