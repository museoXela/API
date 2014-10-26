from authentication import OAuth20Authentication
from tastypie.resources import Resource
from tastypie.authorization import DjangoAuthorization

class Busqueda(Resource):
    
    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.throttle_check(request)
        keyword = kwargs['keyword']
        investigaciones = [], piezas = [], categorias = []
        investigaciones = self.get_investigaciones(keyword, request)
        piezas = self.get_piezas(keyword, request)
        categorias = self.get_piezas_categoria(keyword, request)
        piezas.append(categorias)
        response = {'piezas':piezas, 'investigaciones':investigaciones}
        self.log_throttled_access(request)
        return self.create_response(request, response)
        
    def get_piezas_categoria(self, titulo, request):
        from colecciones.models import Categoria
        from piezas.resources import Exhibicion
        from piezas.models import Pieza
        from tastypie.paginator import Paginator
        res = Exhibicion()
        cat = Categoria.objects.get(nombre=titulo)
        objects = Pieza.objects.filter(exhibicion=True).filter(categoria=cat)
        list = Paginator(request.GET, objects).page()['objects']
        for obj in list:
            bundle = res.build_bundle(obj=obj, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(obj)
        return objects
    
    def get_piezas(self,titulo, request):
        from piezas.models import Pieza 
        from piezas.resources import Exhibicion
        from tastypie.paginator import Paginator
        res = Exhibicion()
        objects = Pieza.objects.filter(exhibicion=True).filter(nombre__contains=titulo)
        list = Paginator(request.GET, objects).page()['objects']
        for obj in list:
            bundle = res.build_bundle(obj=obj, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(obj)
        return objects
    def get_investigaciones(self, titulo, request):
        from investigacion.models import Investigacion as Investigaciones
        from investigacion.resources import Investigacion
        from tastypie.paginator import Paginator
        res = Investigacion()
        objects = Investigaciones.objects.filter(titulo__contains=titulo)
        list = Paginator(request.GET, objects).page()['objects']
        for obj in list:
            bundle = res.build_bundle(obj=obj, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)
        return objects