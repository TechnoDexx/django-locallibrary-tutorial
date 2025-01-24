from ninja import NinjaAPI
api=NinjaAPI()

@api.get("/hello")
async def Hello(request):
  return {"message":"Hello World"}
