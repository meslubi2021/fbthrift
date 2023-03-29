// @generated by Thrift for [[[ program path ]]]
// This file is probably not the place you want to edit!

package module // [[[ program thrift source path ]]]


import (
    "context"
    "fmt"

    cpp "thrift/annotation/cpp"
    python "thrift/annotation/python"
    thrift0 "thrift/annotation/thrift"
    scope "thrift/annotation/scope"
    hack "thrift/annotation/hack"
    rust "thrift/annotation/rust"

    "thrift/lib/go/thrift"
)

var _ = cpp.GoUnusedProtection__
var _ = python.GoUnusedProtection__
var _ = thrift0.GoUnusedProtection__
var _ = scope.GoUnusedProtection__
var _ = hack.GoUnusedProtection__
var _ = rust.GoUnusedProtection__

// (needed to ensure safety because of naive import list construction)
var _ = context.Background
var _ = fmt.Printf
var _ = thrift.ZERO



type Service interface {
    Func(ctx context.Context, arg1 StringWithAdapter, arg2 string, arg3 *Foo) (MyI32, error)
}

// Deprecated: Use Service instead.
type ServiceClientInterface interface {
    thrift.ClientInterface
    Func(arg1 StringWithAdapter, arg2 string, arg3 *Foo) (MyI32, error)
}

type ServiceChannelClient struct {
    ch thrift.RequestChannel
}
// Compile time interface enforcer
var _ Service = &ServiceChannelClient{}

func NewServiceChannelClient(channel thrift.RequestChannel) *ServiceChannelClient {
    return &ServiceChannelClient{
        ch: channel,
    }
}

func (c *ServiceChannelClient) Close() error {
    return c.ch.Close()
}

func (c *ServiceChannelClient) IsOpen() bool {
    return c.ch.IsOpen()
}

func (c *ServiceChannelClient) Open() error {
    return c.ch.Open()
}

// Deprecated: Use ServiceChannelClient instead.
type ServiceClient struct {
    chClient *ServiceChannelClient
}
// Compile time interface enforcer
var _ ServiceClientInterface = &ServiceClient{}

// Deprecated: Use NewServiceChannelClient() instead.
func NewServiceClient(t thrift.Transport, iprot thrift.Protocol, oprot thrift.Protocol) *ServiceClient {
    return &ServiceClient{
        chClient: NewServiceChannelClient(
            thrift.NewSerialChannel(iprot),
        ),
    }
}

func (c *ServiceClient) Close() error {
    return c.chClient.Close()
}

func (c *ServiceClient) IsOpen() bool {
    return c.chClient.IsOpen()
}

func (c *ServiceClient) Open() error {
    return c.chClient.Open()
}

// Deprecated: Use ServiceChannelClient instead.
type ServiceThreadsafeClient = ServiceClient

// Deprecated: Use NewServiceChannelClient() instead.
func NewServiceThreadsafeClient(t thrift.Transport, iprot thrift.Protocol, oprot thrift.Protocol) *ServiceThreadsafeClient {
    return NewServiceClient(t, iprot, oprot)
}

// Deprecated: Use NewServiceChannelClient() instead.
func NewServiceClientProtocol(prot thrift.Protocol) *ServiceClient {
  return NewServiceClient(prot.Transport(), prot, prot)
}

// Deprecated: Use NewServiceChannelClient() instead.
func NewServiceThreadsafeClientProtocol(prot thrift.Protocol) *ServiceClient {
  return NewServiceClient(prot.Transport(), prot, prot)
}

// Deprecated: Use NewServiceChannelClient() instead.
func NewServiceClientFactory(t thrift.Transport, pf thrift.ProtocolFactory) *ServiceClient {
  iprot := pf.GetProtocol(t)
  oprot := pf.GetProtocol(t)
  return NewServiceClient(t, iprot, oprot)
}

// Deprecated: Use NewServiceChannelClient() instead.
func NewServiceThreadsafeClientFactory(t thrift.Transport, pf thrift.ProtocolFactory) *ServiceThreadsafeClient {
  return NewServiceClientFactory(t, pf)
}


func (c *ServiceChannelClient) Func(ctx context.Context, arg1 StringWithAdapter, arg2 string, arg3 *Foo) (MyI32, error) {
    in := &reqServiceFunc{
        Arg1: arg1,
        Arg2: arg2,
        Arg3: arg3,
    }
    out := newRespServiceFunc()
    err := c.ch.Call(ctx, "func", in, out)
    return out.Value, err
}

func (c *ServiceClient) Func(arg1 StringWithAdapter, arg2 string, arg3 *Foo) (MyI32, error) {
    return c.chClient.Func(nil, arg1, arg2, arg3)
}


type reqServiceFunc struct {
    Arg1 StringWithAdapter `thrift:"arg1,1" json:"arg1" db:"arg1"`
    Arg2 string `thrift:"arg2,2" json:"arg2" db:"arg2"`
    Arg3 *Foo `thrift:"arg3,3" json:"arg3" db:"arg3"`
}
// Compile time interface enforcer
var _ thrift.Struct = &reqServiceFunc{}

func newReqServiceFunc() *reqServiceFunc {
    return (&reqServiceFunc{})
}

// Deprecated: Use newReqServiceFunc().Arg3 instead.
var reqServiceFunc_Arg3_DEFAULT = newReqServiceFunc().Arg3

func (x *reqServiceFunc) GetArg1NonCompat() StringWithAdapter {
    return x.Arg1
}

func (x *reqServiceFunc) GetArg1() StringWithAdapter {
    return x.Arg1
}

func (x *reqServiceFunc) GetArg2NonCompat() string {
    return x.Arg2
}

func (x *reqServiceFunc) GetArg2() string {
    return x.Arg2
}

func (x *reqServiceFunc) GetArg3NonCompat() *Foo {
    return x.Arg3
}

func (x *reqServiceFunc) GetArg3() *Foo {
    if !x.IsSetArg3() {
      return NewFoo()
    }

    return x.Arg3
}

func (x *reqServiceFunc) SetArg1(value StringWithAdapter) *reqServiceFunc {
    x.Arg1 = value
    return x
}

func (x *reqServiceFunc) SetArg2(value string) *reqServiceFunc {
    x.Arg2 = value
    return x
}

func (x *reqServiceFunc) SetArg3(value Foo) *reqServiceFunc {
    x.Arg3 = &value
    return x
}



func (x *reqServiceFunc) IsSetArg3() bool {
    return x.Arg3 != nil
}

func (x *reqServiceFunc) writeField1(p thrift.Protocol) error {  // Arg1
    if err := p.WriteFieldBegin("arg1", thrift.STRING, 1); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.GetArg1NonCompat()
    err := WriteStringWithAdapter(item, p)
if err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *reqServiceFunc) writeField2(p thrift.Protocol) error {  // Arg2
    if err := p.WriteFieldBegin("arg2", thrift.STRING, 2); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.GetArg2NonCompat()
    if err := p.WriteString(item); err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *reqServiceFunc) writeField3(p thrift.Protocol) error {  // Arg3
    if !x.IsSetArg3() {
        return nil
    }

    if err := p.WriteFieldBegin("arg3", thrift.STRUCT, 3); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.GetArg3NonCompat()
    if err := item.Write(p); err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *reqServiceFunc) readField1(p thrift.Protocol) error {  // Arg1
    result, err := ReadStringWithAdapter(p)
if err != nil {
    return err
}

    x.SetArg1(result)
    return nil
}

func (x *reqServiceFunc) readField2(p thrift.Protocol) error {  // Arg2
    result, err := p.ReadString()
if err != nil {
    return err
}

    x.SetArg2(result)
    return nil
}

func (x *reqServiceFunc) readField3(p thrift.Protocol) error {  // Arg3
    result := *NewFoo()
err := result.Read(p)
if err != nil {
    return err
}

    x.SetArg3(result)
    return nil
}

func (x *reqServiceFunc) String() string {
    return fmt.Sprintf("%+v", x)
}


// Deprecated: Use reqServiceFunc.Set* methods instead or set the fields directly.
type reqServiceFuncBuilder struct {
    obj *reqServiceFunc
}

func newReqServiceFuncBuilder() *reqServiceFuncBuilder {
    return &reqServiceFuncBuilder{
        obj: newReqServiceFunc(),
    }
}

func (x *reqServiceFuncBuilder) Arg1(value StringWithAdapter) *reqServiceFuncBuilder {
    x.obj.Arg1 = value
    return x
}

func (x *reqServiceFuncBuilder) Arg2(value string) *reqServiceFuncBuilder {
    x.obj.Arg2 = value
    return x
}

func (x *reqServiceFuncBuilder) Arg3(value *Foo) *reqServiceFuncBuilder {
    x.obj.Arg3 = value
    return x
}

func (x *reqServiceFuncBuilder) Emit() *reqServiceFunc {
    var objCopy reqServiceFunc = *x.obj
    return &objCopy
}

func (x *reqServiceFunc) Write(p thrift.Protocol) error {
    if err := p.WriteStructBegin("reqServiceFunc"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }

    if err := x.writeField1(p); err != nil {
        return err
    }

    if err := x.writeField2(p); err != nil {
        return err
    }

    if err := x.writeField3(p); err != nil {
        return err
    }

    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *reqServiceFunc) Read(p thrift.Protocol) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, typ, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if typ == thrift.STOP {
            break;
        }

        switch id {
        case 1:  // arg1
            if err := x.readField1(p); err != nil {
                return err
            }
        case 2:  // arg2
            if err := x.readField2(p); err != nil {
                return err
            }
        case 3:  // arg3
            if err := x.readField3(p); err != nil {
                return err
            }
        default:
            if err := p.Skip(typ); err != nil {
                return err
            }
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}

type respServiceFunc struct {
    Value MyI32 `thrift:"value,0" json:"value" db:"value"`
}
// Compile time interface enforcer
var _ thrift.Struct = &respServiceFunc{}

func newRespServiceFunc() *respServiceFunc {
    return (&respServiceFunc{})
}

func (x *respServiceFunc) GetValueNonCompat() MyI32 {
    return x.Value
}

func (x *respServiceFunc) GetValue() MyI32 {
    return x.Value
}

func (x *respServiceFunc) SetValue(value MyI32) *respServiceFunc {
    x.Value = value
    return x
}


func (x *respServiceFunc) writeField0(p thrift.Protocol) error {  // Value
    if err := p.WriteFieldBegin("value", thrift.I32, 0); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.GetValueNonCompat()
    err := WriteMyI32(item, p)
if err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *respServiceFunc) readField0(p thrift.Protocol) error {  // Value
    result, err := ReadMyI32(p)
if err != nil {
    return err
}

    x.SetValue(result)
    return nil
}

func (x *respServiceFunc) String() string {
    return fmt.Sprintf("%+v", x)
}


// Deprecated: Use respServiceFunc.Set* methods instead or set the fields directly.
type respServiceFuncBuilder struct {
    obj *respServiceFunc
}

func newRespServiceFuncBuilder() *respServiceFuncBuilder {
    return &respServiceFuncBuilder{
        obj: newRespServiceFunc(),
    }
}

func (x *respServiceFuncBuilder) Value(value MyI32) *respServiceFuncBuilder {
    x.obj.Value = value
    return x
}

func (x *respServiceFuncBuilder) Emit() *respServiceFunc {
    var objCopy respServiceFunc = *x.obj
    return &objCopy
}

func (x *respServiceFunc) Write(p thrift.Protocol) error {
    if err := p.WriteStructBegin("respServiceFunc"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }

    if err := x.writeField0(p); err != nil {
        return err
    }

    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *respServiceFunc) Read(p thrift.Protocol) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, typ, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if typ == thrift.STOP {
            break;
        }

        switch id {
        case 0:  // value
            if err := x.readField0(p); err != nil {
                return err
            }
        default:
            if err := p.Skip(typ); err != nil {
                return err
            }
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}



type ServiceProcessor struct {
    processorMap       map[string]thrift.ProcessorFunction
    functionServiceMap map[string]string
    handler            Service
}
// Compile time interface enforcer
var _ thrift.Processor = &ServiceProcessor{}

func (p *ServiceProcessor) AddToProcessorMap(key string, processor thrift.ProcessorFunction) {
    p.processorMap[key] = processor
}

func (p *ServiceProcessor) AddToFunctionServiceMap(key, service string) {
    p.functionServiceMap[key] = service
}

func (p *ServiceProcessor) GetProcessorFunction(key string) (processor thrift.ProcessorFunction, err error) {
    if processor, ok := p.processorMap[key]; ok {
        return processor, nil
    }
    return nil, nil
}

func (p *ServiceProcessor) ProcessorMap() map[string]thrift.ProcessorFunction {
    return p.processorMap
}

func (p *ServiceProcessor) FunctionServiceMap() map[string]string {
    return p.functionServiceMap
}

func NewServiceProcessor(handler Service) *ServiceProcessor {
    p := &ServiceProcessor{
        handler:            handler,
        processorMap:       make(map[string]thrift.ProcessorFunction),
        functionServiceMap: make(map[string]string),
    }
    p.AddToProcessorMap("func", &procFuncServiceFunc{handler: handler})
    p.AddToFunctionServiceMap("func", "Service")

    return p
}


type procFuncServiceFunc struct {
    handler Service
}
// Compile time interface enforcer
var _ thrift.ProcessorFunction = &procFuncServiceFunc{}

func (p *procFuncServiceFunc) Read(iprot thrift.Protocol) (thrift.Struct, thrift.Exception) {
    args := newReqServiceFunc()
    if err := args.Read(iprot); err != nil {
        return nil, err
    }
    iprot.ReadMessageEnd()
    return args, nil
}

func (p *procFuncServiceFunc) Write(seqId int32, result thrift.WritableStruct, oprot thrift.Protocol) (err thrift.Exception) {
    var err2 error
    messageType := thrift.REPLY
    if _, ok := result.(thrift.ApplicationException); ok {
        messageType = thrift.EXCEPTION
    }
    if err2 = oprot.WriteMessageBegin("Func", messageType, seqId); err2 != nil {
        err = err2
    }
    if err2 = result.Write(oprot); err == nil && err2 != nil {
        err = err2
    }
    if err2 = oprot.WriteMessageEnd(); err == nil && err2 != nil {
        err = err2
    }
    if err2 = oprot.Flush(); err == nil && err2 != nil {
        err = err2
    }
    return err
}

func (p *procFuncServiceFunc) Run(reqStruct thrift.Struct) (thrift.WritableStruct, thrift.ApplicationException) {
    args := reqStruct.(*reqServiceFunc)
    result := newRespServiceFunc()
    retval, err := p.handler.Func(args.Arg1, args.Arg2, args.Arg3)
    if err != nil {
        x := thrift.NewApplicationExceptionCause(thrift.INTERNAL_ERROR, "Internal error processing Func: " + err.Error(), err)
        return x, x
    }

    result.Value = retval
    return result, nil
}




type AdapterService interface {
    Count(ctx context.Context) (*CountingStruct, error)
    AdaptedTypes(ctx context.Context, arg *HeapAllocated) (*HeapAllocated, error)
}

// Deprecated: Use AdapterService instead.
type AdapterServiceClientInterface interface {
    thrift.ClientInterface
    Count() (*CountingStruct, error)
    AdaptedTypes(arg *HeapAllocated) (*HeapAllocated, error)
}

type AdapterServiceChannelClient struct {
    ch thrift.RequestChannel
}
// Compile time interface enforcer
var _ AdapterService = &AdapterServiceChannelClient{}

func NewAdapterServiceChannelClient(channel thrift.RequestChannel) *AdapterServiceChannelClient {
    return &AdapterServiceChannelClient{
        ch: channel,
    }
}

func (c *AdapterServiceChannelClient) Close() error {
    return c.ch.Close()
}

func (c *AdapterServiceChannelClient) IsOpen() bool {
    return c.ch.IsOpen()
}

func (c *AdapterServiceChannelClient) Open() error {
    return c.ch.Open()
}

// Deprecated: Use AdapterServiceChannelClient instead.
type AdapterServiceClient struct {
    chClient *AdapterServiceChannelClient
}
// Compile time interface enforcer
var _ AdapterServiceClientInterface = &AdapterServiceClient{}

// Deprecated: Use NewAdapterServiceChannelClient() instead.
func NewAdapterServiceClient(t thrift.Transport, iprot thrift.Protocol, oprot thrift.Protocol) *AdapterServiceClient {
    return &AdapterServiceClient{
        chClient: NewAdapterServiceChannelClient(
            thrift.NewSerialChannel(iprot),
        ),
    }
}

func (c *AdapterServiceClient) Close() error {
    return c.chClient.Close()
}

func (c *AdapterServiceClient) IsOpen() bool {
    return c.chClient.IsOpen()
}

func (c *AdapterServiceClient) Open() error {
    return c.chClient.Open()
}

// Deprecated: Use AdapterServiceChannelClient instead.
type AdapterServiceThreadsafeClient = AdapterServiceClient

// Deprecated: Use NewAdapterServiceChannelClient() instead.
func NewAdapterServiceThreadsafeClient(t thrift.Transport, iprot thrift.Protocol, oprot thrift.Protocol) *AdapterServiceThreadsafeClient {
    return NewAdapterServiceClient(t, iprot, oprot)
}

// Deprecated: Use NewAdapterServiceChannelClient() instead.
func NewAdapterServiceClientProtocol(prot thrift.Protocol) *AdapterServiceClient {
  return NewAdapterServiceClient(prot.Transport(), prot, prot)
}

// Deprecated: Use NewAdapterServiceChannelClient() instead.
func NewAdapterServiceThreadsafeClientProtocol(prot thrift.Protocol) *AdapterServiceClient {
  return NewAdapterServiceClient(prot.Transport(), prot, prot)
}

// Deprecated: Use NewAdapterServiceChannelClient() instead.
func NewAdapterServiceClientFactory(t thrift.Transport, pf thrift.ProtocolFactory) *AdapterServiceClient {
  iprot := pf.GetProtocol(t)
  oprot := pf.GetProtocol(t)
  return NewAdapterServiceClient(t, iprot, oprot)
}

// Deprecated: Use NewAdapterServiceChannelClient() instead.
func NewAdapterServiceThreadsafeClientFactory(t thrift.Transport, pf thrift.ProtocolFactory) *AdapterServiceThreadsafeClient {
  return NewAdapterServiceClientFactory(t, pf)
}


func (c *AdapterServiceChannelClient) Count(ctx context.Context) (*CountingStruct, error) {
    in := &reqAdapterServiceCount{
    }
    out := newRespAdapterServiceCount()
    err := c.ch.Call(ctx, "count", in, out)
    return out.Value, err
}

func (c *AdapterServiceClient) Count() (*CountingStruct, error) {
    return c.chClient.Count(nil)
}


func (c *AdapterServiceChannelClient) AdaptedTypes(ctx context.Context, arg *HeapAllocated) (*HeapAllocated, error) {
    in := &reqAdapterServiceAdaptedTypes{
        Arg_: arg,
    }
    out := newRespAdapterServiceAdaptedTypes()
    err := c.ch.Call(ctx, "adaptedTypes", in, out)
    return out.Value, err
}

func (c *AdapterServiceClient) AdaptedTypes(arg *HeapAllocated) (*HeapAllocated, error) {
    return c.chClient.AdaptedTypes(nil, arg)
}


type reqAdapterServiceCount struct {
}
// Compile time interface enforcer
var _ thrift.Struct = &reqAdapterServiceCount{}

func newReqAdapterServiceCount() *reqAdapterServiceCount {
    return (&reqAdapterServiceCount{})
}

func (x *reqAdapterServiceCount) String() string {
    return fmt.Sprintf("%+v", x)
}


// Deprecated: Use reqAdapterServiceCount.Set* methods instead or set the fields directly.
type reqAdapterServiceCountBuilder struct {
    obj *reqAdapterServiceCount
}

func newReqAdapterServiceCountBuilder() *reqAdapterServiceCountBuilder {
    return &reqAdapterServiceCountBuilder{
        obj: newReqAdapterServiceCount(),
    }
}

func (x *reqAdapterServiceCountBuilder) Emit() *reqAdapterServiceCount {
    var objCopy reqAdapterServiceCount = *x.obj
    return &objCopy
}

func (x *reqAdapterServiceCount) Write(p thrift.Protocol) error {
    if err := p.WriteStructBegin("reqAdapterServiceCount"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }

    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *reqAdapterServiceCount) Read(p thrift.Protocol) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, typ, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if typ == thrift.STOP {
            break;
        }

        switch id {
        default:
            if err := p.Skip(typ); err != nil {
                return err
            }
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}

type respAdapterServiceCount struct {
    Value *CountingStruct `thrift:"value,0" json:"value" db:"value"`
}
// Compile time interface enforcer
var _ thrift.Struct = &respAdapterServiceCount{}

func newRespAdapterServiceCount() *respAdapterServiceCount {
    return (&respAdapterServiceCount{})
}

// Deprecated: Use newRespAdapterServiceCount().Value instead.
var respAdapterServiceCount_Value_DEFAULT = newRespAdapterServiceCount().Value

func (x *respAdapterServiceCount) GetValueNonCompat() *CountingStruct {
    return x.Value
}

func (x *respAdapterServiceCount) GetValue() *CountingStruct {
    if !x.IsSetValue() {
      return NewCountingStruct()
    }

    return x.Value
}

func (x *respAdapterServiceCount) SetValue(value CountingStruct) *respAdapterServiceCount {
    x.Value = &value
    return x
}

func (x *respAdapterServiceCount) IsSetValue() bool {
    return x.Value != nil
}

func (x *respAdapterServiceCount) writeField0(p thrift.Protocol) error {  // Value
    if !x.IsSetValue() {
        return nil
    }

    if err := p.WriteFieldBegin("value", thrift.STRUCT, 0); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.GetValueNonCompat()
    if err := item.Write(p); err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *respAdapterServiceCount) readField0(p thrift.Protocol) error {  // Value
    result := *NewCountingStruct()
err := result.Read(p)
if err != nil {
    return err
}

    x.SetValue(result)
    return nil
}

func (x *respAdapterServiceCount) String() string {
    return fmt.Sprintf("%+v", x)
}


// Deprecated: Use respAdapterServiceCount.Set* methods instead or set the fields directly.
type respAdapterServiceCountBuilder struct {
    obj *respAdapterServiceCount
}

func newRespAdapterServiceCountBuilder() *respAdapterServiceCountBuilder {
    return &respAdapterServiceCountBuilder{
        obj: newRespAdapterServiceCount(),
    }
}

func (x *respAdapterServiceCountBuilder) Value(value *CountingStruct) *respAdapterServiceCountBuilder {
    x.obj.Value = value
    return x
}

func (x *respAdapterServiceCountBuilder) Emit() *respAdapterServiceCount {
    var objCopy respAdapterServiceCount = *x.obj
    return &objCopy
}

func (x *respAdapterServiceCount) Write(p thrift.Protocol) error {
    if err := p.WriteStructBegin("respAdapterServiceCount"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }

    if err := x.writeField0(p); err != nil {
        return err
    }

    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *respAdapterServiceCount) Read(p thrift.Protocol) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, typ, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if typ == thrift.STOP {
            break;
        }

        switch id {
        case 0:  // value
            if err := x.readField0(p); err != nil {
                return err
            }
        default:
            if err := p.Skip(typ); err != nil {
                return err
            }
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}

type reqAdapterServiceAdaptedTypes struct {
    Arg_ *HeapAllocated `thrift:"arg,1" json:"arg" db:"arg"`
}
// Compile time interface enforcer
var _ thrift.Struct = &reqAdapterServiceAdaptedTypes{}

func newReqAdapterServiceAdaptedTypes() *reqAdapterServiceAdaptedTypes {
    return (&reqAdapterServiceAdaptedTypes{})
}

// Deprecated: Use newReqAdapterServiceAdaptedTypes().Arg_ instead.
var reqAdapterServiceAdaptedTypes_Arg__DEFAULT = newReqAdapterServiceAdaptedTypes().Arg_

func (x *reqAdapterServiceAdaptedTypes) GetArg_NonCompat() *HeapAllocated {
    return x.Arg_
}

func (x *reqAdapterServiceAdaptedTypes) GetArg_() *HeapAllocated {
    if !x.IsSetArg_() {
      return NewHeapAllocated()
    }

    return x.Arg_
}

func (x *reqAdapterServiceAdaptedTypes) SetArg_(value HeapAllocated) *reqAdapterServiceAdaptedTypes {
    x.Arg_ = &value
    return x
}

func (x *reqAdapterServiceAdaptedTypes) IsSetArg_() bool {
    return x.Arg_ != nil
}

func (x *reqAdapterServiceAdaptedTypes) writeField1(p thrift.Protocol) error {  // Arg_
    if !x.IsSetArg_() {
        return nil
    }

    if err := p.WriteFieldBegin("arg", thrift.STRUCT, 1); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.GetArg_NonCompat()
    if err := item.Write(p); err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *reqAdapterServiceAdaptedTypes) readField1(p thrift.Protocol) error {  // Arg_
    result := *NewHeapAllocated()
err := result.Read(p)
if err != nil {
    return err
}

    x.SetArg_(result)
    return nil
}

func (x *reqAdapterServiceAdaptedTypes) String() string {
    return fmt.Sprintf("%+v", x)
}


// Deprecated: Use reqAdapterServiceAdaptedTypes.Set* methods instead or set the fields directly.
type reqAdapterServiceAdaptedTypesBuilder struct {
    obj *reqAdapterServiceAdaptedTypes
}

func newReqAdapterServiceAdaptedTypesBuilder() *reqAdapterServiceAdaptedTypesBuilder {
    return &reqAdapterServiceAdaptedTypesBuilder{
        obj: newReqAdapterServiceAdaptedTypes(),
    }
}

func (x *reqAdapterServiceAdaptedTypesBuilder) Arg_(value *HeapAllocated) *reqAdapterServiceAdaptedTypesBuilder {
    x.obj.Arg_ = value
    return x
}

func (x *reqAdapterServiceAdaptedTypesBuilder) Emit() *reqAdapterServiceAdaptedTypes {
    var objCopy reqAdapterServiceAdaptedTypes = *x.obj
    return &objCopy
}

func (x *reqAdapterServiceAdaptedTypes) Write(p thrift.Protocol) error {
    if err := p.WriteStructBegin("reqAdapterServiceAdaptedTypes"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }

    if err := x.writeField1(p); err != nil {
        return err
    }

    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *reqAdapterServiceAdaptedTypes) Read(p thrift.Protocol) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, typ, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if typ == thrift.STOP {
            break;
        }

        switch id {
        case 1:  // arg
            if err := x.readField1(p); err != nil {
                return err
            }
        default:
            if err := p.Skip(typ); err != nil {
                return err
            }
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}

type respAdapterServiceAdaptedTypes struct {
    Value *HeapAllocated `thrift:"value,0" json:"value" db:"value"`
}
// Compile time interface enforcer
var _ thrift.Struct = &respAdapterServiceAdaptedTypes{}

func newRespAdapterServiceAdaptedTypes() *respAdapterServiceAdaptedTypes {
    return (&respAdapterServiceAdaptedTypes{})
}

// Deprecated: Use newRespAdapterServiceAdaptedTypes().Value instead.
var respAdapterServiceAdaptedTypes_Value_DEFAULT = newRespAdapterServiceAdaptedTypes().Value

func (x *respAdapterServiceAdaptedTypes) GetValueNonCompat() *HeapAllocated {
    return x.Value
}

func (x *respAdapterServiceAdaptedTypes) GetValue() *HeapAllocated {
    if !x.IsSetValue() {
      return NewHeapAllocated()
    }

    return x.Value
}

func (x *respAdapterServiceAdaptedTypes) SetValue(value HeapAllocated) *respAdapterServiceAdaptedTypes {
    x.Value = &value
    return x
}

func (x *respAdapterServiceAdaptedTypes) IsSetValue() bool {
    return x.Value != nil
}

func (x *respAdapterServiceAdaptedTypes) writeField0(p thrift.Protocol) error {  // Value
    if !x.IsSetValue() {
        return nil
    }

    if err := p.WriteFieldBegin("value", thrift.STRUCT, 0); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.GetValueNonCompat()
    if err := item.Write(p); err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *respAdapterServiceAdaptedTypes) readField0(p thrift.Protocol) error {  // Value
    result := *NewHeapAllocated()
err := result.Read(p)
if err != nil {
    return err
}

    x.SetValue(result)
    return nil
}

func (x *respAdapterServiceAdaptedTypes) String() string {
    return fmt.Sprintf("%+v", x)
}


// Deprecated: Use respAdapterServiceAdaptedTypes.Set* methods instead or set the fields directly.
type respAdapterServiceAdaptedTypesBuilder struct {
    obj *respAdapterServiceAdaptedTypes
}

func newRespAdapterServiceAdaptedTypesBuilder() *respAdapterServiceAdaptedTypesBuilder {
    return &respAdapterServiceAdaptedTypesBuilder{
        obj: newRespAdapterServiceAdaptedTypes(),
    }
}

func (x *respAdapterServiceAdaptedTypesBuilder) Value(value *HeapAllocated) *respAdapterServiceAdaptedTypesBuilder {
    x.obj.Value = value
    return x
}

func (x *respAdapterServiceAdaptedTypesBuilder) Emit() *respAdapterServiceAdaptedTypes {
    var objCopy respAdapterServiceAdaptedTypes = *x.obj
    return &objCopy
}

func (x *respAdapterServiceAdaptedTypes) Write(p thrift.Protocol) error {
    if err := p.WriteStructBegin("respAdapterServiceAdaptedTypes"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }

    if err := x.writeField0(p); err != nil {
        return err
    }

    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *respAdapterServiceAdaptedTypes) Read(p thrift.Protocol) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, typ, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if typ == thrift.STOP {
            break;
        }

        switch id {
        case 0:  // value
            if err := x.readField0(p); err != nil {
                return err
            }
        default:
            if err := p.Skip(typ); err != nil {
                return err
            }
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}



type AdapterServiceProcessor struct {
    processorMap       map[string]thrift.ProcessorFunction
    functionServiceMap map[string]string
    handler            AdapterService
}
// Compile time interface enforcer
var _ thrift.Processor = &AdapterServiceProcessor{}

func (p *AdapterServiceProcessor) AddToProcessorMap(key string, processor thrift.ProcessorFunction) {
    p.processorMap[key] = processor
}

func (p *AdapterServiceProcessor) AddToFunctionServiceMap(key, service string) {
    p.functionServiceMap[key] = service
}

func (p *AdapterServiceProcessor) GetProcessorFunction(key string) (processor thrift.ProcessorFunction, err error) {
    if processor, ok := p.processorMap[key]; ok {
        return processor, nil
    }
    return nil, nil
}

func (p *AdapterServiceProcessor) ProcessorMap() map[string]thrift.ProcessorFunction {
    return p.processorMap
}

func (p *AdapterServiceProcessor) FunctionServiceMap() map[string]string {
    return p.functionServiceMap
}

func NewAdapterServiceProcessor(handler AdapterService) *AdapterServiceProcessor {
    p := &AdapterServiceProcessor{
        handler:            handler,
        processorMap:       make(map[string]thrift.ProcessorFunction),
        functionServiceMap: make(map[string]string),
    }
    p.AddToProcessorMap("count", &procFuncAdapterServiceCount{handler: handler})
    p.AddToProcessorMap("adaptedTypes", &procFuncAdapterServiceAdaptedTypes{handler: handler})
    p.AddToFunctionServiceMap("count", "AdapterService")
    p.AddToFunctionServiceMap("adaptedTypes", "AdapterService")

    return p
}


type procFuncAdapterServiceCount struct {
    handler AdapterService
}
// Compile time interface enforcer
var _ thrift.ProcessorFunction = &procFuncAdapterServiceCount{}

func (p *procFuncAdapterServiceCount) Read(iprot thrift.Protocol) (thrift.Struct, thrift.Exception) {
    args := newReqAdapterServiceCount()
    if err := args.Read(iprot); err != nil {
        return nil, err
    }
    iprot.ReadMessageEnd()
    return args, nil
}

func (p *procFuncAdapterServiceCount) Write(seqId int32, result thrift.WritableStruct, oprot thrift.Protocol) (err thrift.Exception) {
    var err2 error
    messageType := thrift.REPLY
    if _, ok := result.(thrift.ApplicationException); ok {
        messageType = thrift.EXCEPTION
    }
    if err2 = oprot.WriteMessageBegin("Count", messageType, seqId); err2 != nil {
        err = err2
    }
    if err2 = result.Write(oprot); err == nil && err2 != nil {
        err = err2
    }
    if err2 = oprot.WriteMessageEnd(); err == nil && err2 != nil {
        err = err2
    }
    if err2 = oprot.Flush(); err == nil && err2 != nil {
        err = err2
    }
    return err
}

func (p *procFuncAdapterServiceCount) Run(reqStruct thrift.Struct) (thrift.WritableStruct, thrift.ApplicationException) {
    result := newRespAdapterServiceCount()
    retval, err := p.handler.Count()
    if err != nil {
        x := thrift.NewApplicationExceptionCause(thrift.INTERNAL_ERROR, "Internal error processing Count: " + err.Error(), err)
        return x, x
    }

    result.Value = retval
    return result, nil
}


type procFuncAdapterServiceAdaptedTypes struct {
    handler AdapterService
}
// Compile time interface enforcer
var _ thrift.ProcessorFunction = &procFuncAdapterServiceAdaptedTypes{}

func (p *procFuncAdapterServiceAdaptedTypes) Read(iprot thrift.Protocol) (thrift.Struct, thrift.Exception) {
    args := newReqAdapterServiceAdaptedTypes()
    if err := args.Read(iprot); err != nil {
        return nil, err
    }
    iprot.ReadMessageEnd()
    return args, nil
}

func (p *procFuncAdapterServiceAdaptedTypes) Write(seqId int32, result thrift.WritableStruct, oprot thrift.Protocol) (err thrift.Exception) {
    var err2 error
    messageType := thrift.REPLY
    if _, ok := result.(thrift.ApplicationException); ok {
        messageType = thrift.EXCEPTION
    }
    if err2 = oprot.WriteMessageBegin("AdaptedTypes", messageType, seqId); err2 != nil {
        err = err2
    }
    if err2 = result.Write(oprot); err == nil && err2 != nil {
        err = err2
    }
    if err2 = oprot.WriteMessageEnd(); err == nil && err2 != nil {
        err = err2
    }
    if err2 = oprot.Flush(); err == nil && err2 != nil {
        err = err2
    }
    return err
}

func (p *procFuncAdapterServiceAdaptedTypes) Run(reqStruct thrift.Struct) (thrift.WritableStruct, thrift.ApplicationException) {
    args := reqStruct.(*reqAdapterServiceAdaptedTypes)
    result := newRespAdapterServiceAdaptedTypes()
    retval, err := p.handler.AdaptedTypes(args.Arg_)
    if err != nil {
        x := thrift.NewApplicationExceptionCause(thrift.INTERNAL_ERROR, "Internal error processing AdaptedTypes: " + err.Error(), err)
        return x, x
    }

    result.Value = retval
    return result, nil
}


