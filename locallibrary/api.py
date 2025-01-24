from ninja import NinjaAPI
from typing import Union
api=NinjaAPI()

@api.get("/")
async def index(request):
  return {"message":"Hello World"}
@api.get("/hello")
async def Hello(request,name="World"):
  return {"message":f"Hello {name}"}
@api.get("/math")
async def math(request, a:Union[int,None]=None,b:Union[int, None]=None):
  if not(a is None) and not(b is None):
    return {"add":a+b,"multiply":a*b,"divide":a/b,"subtract":a-b}
  else:
    return {"message":"Please enter two numbers"}
