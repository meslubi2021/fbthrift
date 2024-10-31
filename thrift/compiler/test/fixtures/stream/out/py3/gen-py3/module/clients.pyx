#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/stream/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
from libc.stdint cimport (
    int8_t as cint8_t,
    int16_t as cint16_t,
    int32_t as cint32_t,
    int64_t as cint64_t,
)
from libcpp.memory cimport shared_ptr, make_shared, unique_ptr
from libcpp.string cimport string
from libcpp cimport bool as cbool
from cpython cimport bool as pbool
from libcpp.vector cimport vector
from libcpp.set cimport set as cset
from libcpp.map cimport map as cmap
from libcpp.utility cimport move as cmove
from cython.operator cimport dereference as deref, typeid
from cpython.ref cimport PyObject
from thrift.py3.client cimport cRequestChannel_ptr, makeClientWrapper, cClientWrapper
from thrift.py3.exceptions cimport try_make_shared_exception
from thrift.python.exceptions cimport create_py_exception
from folly cimport cFollyTry, cFollyUnit, c_unit
from folly.cast cimport down_cast_ptr
from libcpp.typeinfo cimport type_info
import thrift.py3.types
cimport thrift.py3.types
from thrift.py3.types cimport make_unique
import thrift.py3.client
cimport thrift.py3.client
from thrift.python.common cimport (
    RpcOptions as __RpcOptions,
    cThriftServiceMetadataResponse as __fbthrift_cThriftServiceMetadataResponse,
    ServiceMetadata,
    MetadataBox as __MetadataBox,
)

from folly.futures cimport bridgeFutureWith
from folly.executor cimport get_executor
cimport folly.iobuf as _fbthrift_iobuf
import folly.iobuf as _fbthrift_iobuf
from folly.iobuf cimport move as move_iobuf
cimport cython

import sys
import types as _py_types
from asyncio import get_event_loop as asyncio_get_event_loop, shield as asyncio_shield, InvalidStateError as asyncio_InvalidStateError

cimport module.types as _module_types
cimport module.cbindings as _module_cbindings
import module.types as _module_types
from thrift.py3.stream cimport cResponseAndClientBufferedStream, cClientBufferedStream

import module.services_reflection as _services_reflection
cimport module.services_reflection as _services_reflection

from module.clients_wrapper cimport cPubSubStreamingServiceAsyncClient, cPubSubStreamingServiceClientWrapper


cdef void PubSubStreamingService_returnstream_callback(
    cFollyTry[cClientBufferedStream[cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ClientBufferedStream__i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_streamthrows_callback(
    cFollyTry[cClientBufferedStream[cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ClientBufferedStream__i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_servicethrows_callback(
    cFollyTry[cClientBufferedStream[cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException[_module_cbindings.cFooEx]():
        try:
            exc = _module_types.FooEx._create_FBTHRIFT_ONLY_DO_NOT_USE(try_make_shared_exception[_module_cbindings.cFooEx](result.exception()))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))
        else:
            pyfuture.set_exception(exc)
    elif result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ClientBufferedStream__i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_servicethrows2_callback(
    cFollyTry[cClientBufferedStream[cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException[_module_cbindings.cFooEx]():
        try:
            exc = _module_types.FooEx._create_FBTHRIFT_ONLY_DO_NOT_USE(try_make_shared_exception[_module_cbindings.cFooEx](result.exception()))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))
        else:
            pyfuture.set_exception(exc)
    elif result.hasException[_module_cbindings.cFooEx2]():
        try:
            exc = _module_types.FooEx2._create_FBTHRIFT_ONLY_DO_NOT_USE(try_make_shared_exception[_module_cbindings.cFooEx2](result.exception()))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))
        else:
            pyfuture.set_exception(exc)
    elif result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ClientBufferedStream__i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_boththrows_callback(
    cFollyTry[cClientBufferedStream[cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException[_module_cbindings.cFooEx]():
        try:
            exc = _module_types.FooEx._create_FBTHRIFT_ONLY_DO_NOT_USE(try_make_shared_exception[_module_cbindings.cFooEx](result.exception()))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))
        else:
            pyfuture.set_exception(exc)
    elif result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ClientBufferedStream__i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_responseandstreamstreamthrows_callback(
    cFollyTry[cResponseAndClientBufferedStream[cint32_t,cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ResponseAndClientBufferedStream__i32_i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_responseandstreamservicethrows_callback(
    cFollyTry[cResponseAndClientBufferedStream[cint32_t,cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException[_module_cbindings.cFooEx]():
        try:
            exc = _module_types.FooEx._create_FBTHRIFT_ONLY_DO_NOT_USE(try_make_shared_exception[_module_cbindings.cFooEx](result.exception()))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))
        else:
            pyfuture.set_exception(exc)
    elif result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ResponseAndClientBufferedStream__i32_i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_responseandstreamboththrows_callback(
    cFollyTry[cResponseAndClientBufferedStream[cint32_t,cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException[_module_cbindings.cFooEx]():
        try:
            exc = _module_types.FooEx._create_FBTHRIFT_ONLY_DO_NOT_USE(try_make_shared_exception[_module_cbindings.cFooEx](result.exception()))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))
        else:
            pyfuture.set_exception(exc)
    elif result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ResponseAndClientBufferedStream__i32_i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void PubSubStreamingService_returnstreamFast_callback(
    cFollyTry[cClientBufferedStream[cint32_t]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_module_types.ClientBufferedStream__i32._fbthrift_create(result.value(), options))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))


cdef object _PubSubStreamingService_annotations = _py_types.MappingProxyType({
})


@cython.auto_pickle(False)
cdef class PubSubStreamingService(thrift.py3.client.Client):
    annotations = _PubSubStreamingService_annotations

    cdef const type_info* _typeid(PubSubStreamingService self):
        return &typeid(cPubSubStreamingServiceAsyncClient)

    cdef bind_client(PubSubStreamingService self, cRequestChannel_ptr&& channel):
        self._client = makeClientWrapper[cPubSubStreamingServiceAsyncClient, cPubSubStreamingServiceClientWrapper](
            cmove(channel)
        )

    @cython.always_allow_keywords(True)
    def returnstream(
            PubSubStreamingService self,
            i32_from not None,
            i32_to not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(i32_from, int):
            raise TypeError(f'i32_from is not a {int !r}.')
        else:
            i32_from = <cint32_t> i32_from
        if not isinstance(i32_to, int):
            raise TypeError(f'i32_to is not a {int !r}.')
        else:
            i32_to = <cint32_t> i32_to
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cClientBufferedStream[cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).returnstream(rpc_options._cpp_obj, 
                i32_from,
                i32_to,
            ),
            PubSubStreamingService_returnstream_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def streamthrows(
            PubSubStreamingService self,
            foo not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(foo, int):
            raise TypeError(f'foo is not a {int !r}.')
        else:
            foo = <cint32_t> foo
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cClientBufferedStream[cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).streamthrows(rpc_options._cpp_obj, 
                foo,
            ),
            PubSubStreamingService_streamthrows_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def servicethrows(
            PubSubStreamingService self,
            foo not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(foo, int):
            raise TypeError(f'foo is not a {int !r}.')
        else:
            foo = <cint32_t> foo
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cClientBufferedStream[cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).servicethrows(rpc_options._cpp_obj, 
                foo,
            ),
            PubSubStreamingService_servicethrows_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def servicethrows2(
            PubSubStreamingService self,
            foo not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(foo, int):
            raise TypeError(f'foo is not a {int !r}.')
        else:
            foo = <cint32_t> foo
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cClientBufferedStream[cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).servicethrows2(rpc_options._cpp_obj, 
                foo,
            ),
            PubSubStreamingService_servicethrows2_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def boththrows(
            PubSubStreamingService self,
            foo not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(foo, int):
            raise TypeError(f'foo is not a {int !r}.')
        else:
            foo = <cint32_t> foo
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cClientBufferedStream[cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).boththrows(rpc_options._cpp_obj, 
                foo,
            ),
            PubSubStreamingService_boththrows_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def responseandstreamstreamthrows(
            PubSubStreamingService self,
            foo not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(foo, int):
            raise TypeError(f'foo is not a {int !r}.')
        else:
            foo = <cint32_t> foo
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cResponseAndClientBufferedStream[cint32_t,cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).responseandstreamstreamthrows(rpc_options._cpp_obj, 
                foo,
            ),
            PubSubStreamingService_responseandstreamstreamthrows_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def responseandstreamservicethrows(
            PubSubStreamingService self,
            foo not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(foo, int):
            raise TypeError(f'foo is not a {int !r}.')
        else:
            foo = <cint32_t> foo
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cResponseAndClientBufferedStream[cint32_t,cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).responseandstreamservicethrows(rpc_options._cpp_obj, 
                foo,
            ),
            PubSubStreamingService_responseandstreamservicethrows_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def responseandstreamboththrows(
            PubSubStreamingService self,
            foo not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(foo, int):
            raise TypeError(f'foo is not a {int !r}.')
        else:
            foo = <cint32_t> foo
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cResponseAndClientBufferedStream[cint32_t,cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).responseandstreamboththrows(rpc_options._cpp_obj, 
                foo,
            ),
            PubSubStreamingService_responseandstreamboththrows_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def returnstreamFast(
            PubSubStreamingService self,
            i32_from not None,
            i32_to not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(i32_from, int):
            raise TypeError(f'i32_from is not a {int !r}.')
        else:
            i32_from = <cint32_t> i32_from
        if not isinstance(i32_to, int):
            raise TypeError(f'i32_to is not a {int !r}.')
        else:
            i32_to = <cint32_t> i32_to
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cClientBufferedStream[cint32_t]](
            self._executor,
            down_cast_ptr[cPubSubStreamingServiceClientWrapper, cClientWrapper](self._client.get()).returnstreamFast(rpc_options._cpp_obj, 
                i32_from,
                i32_to,
            ),
            PubSubStreamingService_returnstreamFast_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)


    @classmethod
    def __get_reflection__(cls):
        return _services_reflection.get_reflection__PubSubStreamingService(for_clients=True)

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftServiceMetadataResponse response
        ServiceMetadata[_services_reflection.cPubSubStreamingServiceSvIf].gen(response)
        return __MetadataBox.box(cmove(deref(response.metadata_ref())))

    @staticmethod
    def __get_thrift_name__():
        return "module.PubSubStreamingService"

