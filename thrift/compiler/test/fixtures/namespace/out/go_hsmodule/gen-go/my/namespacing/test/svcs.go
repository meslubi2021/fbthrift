// Autogenerated by Thrift for thrift/compiler/test/fixtures/namespace/src/hsmodule.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package test


import (
    "context"
    "fmt"
    "reflect"
    "strings"

    thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift/types"
    metadata "github.com/facebook/fbthrift/thrift/lib/thrift/metadata"
)

// (needed to ensure safety because of naive import list construction)
var _ = context.Background
var _ = fmt.Printf
var _ = reflect.Ptr
var _ = strings.Split
var _ = thrift.ZERO
var _ = metadata.GoUnusedProtection__

type HsTestService interface {
    Init(ctx context.Context, int1 int64) (int64, error)
}

type HsTestServiceChannelClientInterface interface {
    thrift.ClientInterface
    HsTestService
}

type HsTestServiceClientInterface interface {
    thrift.ClientInterface
    Init(int1 int64) (int64, error)
}

type HsTestServiceContextClientInterface interface {
    HsTestServiceClientInterface
    InitContext(ctx context.Context, int1 int64) (int64, error)
}

type HsTestServiceChannelClient struct {
    ch thrift.RequestChannel
}
// Compile time interface enforcer
var _ HsTestServiceChannelClientInterface = (*HsTestServiceChannelClient)(nil)

func NewHsTestServiceChannelClient(channel thrift.RequestChannel) *HsTestServiceChannelClient {
    return &HsTestServiceChannelClient{
        ch: channel,
    }
}

func (c *HsTestServiceChannelClient) Close() error {
    return c.ch.Close()
}

type HsTestServiceClient struct {
    chClient *HsTestServiceChannelClient
}
// Compile time interface enforcer
var _ HsTestServiceClientInterface = (*HsTestServiceClient)(nil)
var _ HsTestServiceContextClientInterface = (*HsTestServiceClient)(nil)

func NewHsTestServiceClient(prot thrift.Protocol) *HsTestServiceClient {
    return &HsTestServiceClient{
        chClient: NewHsTestServiceChannelClient(
            thrift.NewSerialChannel(prot),
        ),
    }
}

func (c *HsTestServiceClient) Close() error {
    return c.chClient.Close()
}

func (c *HsTestServiceChannelClient) Init(ctx context.Context, int1 int64) (int64, error) {
    in := &reqHsTestServiceInit{
        Int1: int1,
    }
    out := newRespHsTestServiceInit()
    err := c.ch.Call(ctx, "init", in, out)
    if err != nil {
        return 0, err
    }
    return out.GetSuccess(), nil
}

func (c *HsTestServiceClient) Init(int1 int64) (int64, error) {
    return c.chClient.Init(context.Background(), int1)
}

func (c *HsTestServiceClient) InitContext(ctx context.Context, int1 int64) (int64, error) {
    return c.chClient.Init(ctx, int1)
}

type reqHsTestServiceInit struct {
    Int1 int64 `thrift:"int1,1" json:"int1" db:"int1"`
}
// Compile time interface enforcer
var _ thrift.Struct = (*reqHsTestServiceInit)(nil)

// Deprecated: HsTestServiceInitArgsDeprecated is deprecated, since it is supposed to be internal.
type HsTestServiceInitArgsDeprecated = reqHsTestServiceInit

func newReqHsTestServiceInit() *reqHsTestServiceInit {
    return (&reqHsTestServiceInit{}).setDefaults()
}

func (x *reqHsTestServiceInit) GetInt1() int64 {
    return x.Int1
}

func (x *reqHsTestServiceInit) SetInt1NonCompat(value int64) *reqHsTestServiceInit {
    x.Int1 = value
    return x
}

func (x *reqHsTestServiceInit) SetInt1(value int64) *reqHsTestServiceInit {
    x.Int1 = value
    return x
}

func (x *reqHsTestServiceInit) writeField1(p thrift.Encoder) error {  // Int1
    if err := p.WriteFieldBegin("int1", thrift.I64, 1); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := x.Int1
    if err := p.WriteI64(item); err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *reqHsTestServiceInit) readField1(p thrift.Decoder) error {  // Int1
    result, err := p.ReadI64()
if err != nil {
    return err
}

    x.Int1 = result
    return nil
}

func (x *reqHsTestServiceInit) toString1() string {  // Int1
    return fmt.Sprintf("%v", x.Int1)
}



func (x *reqHsTestServiceInit) Write(p thrift.Encoder) error {
    if err := p.WriteStructBegin("reqHsTestServiceInit"); err != nil {
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

func (x *reqHsTestServiceInit) Read(p thrift.Decoder) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, wireType, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if wireType == thrift.STOP {
            break;
        }

        var fieldReadErr error
        switch {
        case (id == 1 && wireType == thrift.Type(thrift.I64)):  // int1
            fieldReadErr = x.readField1(p)
        default:
            fieldReadErr = p.Skip(wireType)
        }

        if fieldReadErr != nil {
            return fieldReadErr
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

func (x *reqHsTestServiceInit) String() string {
    if x == nil {
        return "<nil>"
    }

    var sb strings.Builder

    sb.WriteString("reqHsTestServiceInit({")
    sb.WriteString(fmt.Sprintf("Int1:%s", x.toString1()))
    sb.WriteString("})")

    return sb.String()
}
func (x *reqHsTestServiceInit) setDefaults() *reqHsTestServiceInit {
    return x.
        SetInt1NonCompat(0)
}

type respHsTestServiceInit struct {
    Success *int64 `thrift:"success,0,optional" json:"success,omitempty" db:"success"`
}
// Compile time interface enforcer
var _ thrift.Struct = (*respHsTestServiceInit)(nil)
var _ thrift.WritableResult = (*respHsTestServiceInit)(nil)

// Deprecated: HsTestServiceInitResultDeprecated is deprecated, since it is supposed to be internal.
type HsTestServiceInitResultDeprecated = respHsTestServiceInit

func newRespHsTestServiceInit() *respHsTestServiceInit {
    return (&respHsTestServiceInit{}).setDefaults()
}

func (x *respHsTestServiceInit) GetSuccess() int64 {
    if !x.IsSetSuccess() {
        return 0
    }
    return *x.Success
}

func (x *respHsTestServiceInit) SetSuccessNonCompat(value int64) *respHsTestServiceInit {
    x.Success = &value
    return x
}

func (x *respHsTestServiceInit) SetSuccess(value *int64) *respHsTestServiceInit {
    x.Success = value
    return x
}

func (x *respHsTestServiceInit) IsSetSuccess() bool {
    return x != nil && x.Success != nil
}

func (x *respHsTestServiceInit) writeField0(p thrift.Encoder) error {  // Success
    if !x.IsSetSuccess() {
        return nil
    }

    if err := p.WriteFieldBegin("success", thrift.I64, 0); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field begin error: ", x), err)
    }

    item := *x.Success
    if err := p.WriteI64(item); err != nil {
    return err
}

    if err := p.WriteFieldEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field end error: ", x), err)
    }
    return nil
}

func (x *respHsTestServiceInit) readField0(p thrift.Decoder) error {  // Success
    result, err := p.ReadI64()
if err != nil {
    return err
}

    x.Success = &result
    return nil
}

func (x *respHsTestServiceInit) toString0() string {  // Success
    if x.IsSetSuccess() {
        return fmt.Sprintf("%v", *x.Success)
    }
    return fmt.Sprintf("%v", x.Success)
}




func (x *respHsTestServiceInit) Exception() thrift.WritableException {
    return nil
}

func (x *respHsTestServiceInit) Write(p thrift.Encoder) error {
    if err := p.WriteStructBegin("respHsTestServiceInit"); err != nil {
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

func (x *respHsTestServiceInit) Read(p thrift.Decoder) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, wireType, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if wireType == thrift.STOP {
            break;
        }

        var fieldReadErr error
        switch {
        case (id == 0 && wireType == thrift.Type(thrift.I64)):  // success
            fieldReadErr = x.readField0(p)
        default:
            fieldReadErr = p.Skip(wireType)
        }

        if fieldReadErr != nil {
            return fieldReadErr
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

func (x *respHsTestServiceInit) String() string {
    if x == nil {
        return "<nil>"
    }

    var sb strings.Builder

    sb.WriteString("respHsTestServiceInit({")
    sb.WriteString(fmt.Sprintf("Success:%s", x.toString0()))
    sb.WriteString("})")

    return sb.String()
}
func (x *respHsTestServiceInit) setDefaults() *respHsTestServiceInit {
    return x
}



type HsTestServiceProcessor struct {
    processorFunctionMap map[string]thrift.ProcessorFunction
    functionServiceMap   map[string]string
    handler            HsTestService
}
// Compile time interface enforcer
var _ thrift.Processor = (*HsTestServiceProcessor)(nil)

func NewHsTestServiceProcessor(handler HsTestService) *HsTestServiceProcessor {
    p := &HsTestServiceProcessor{
        handler:              handler,
        processorFunctionMap: make(map[string]thrift.ProcessorFunction),
        functionServiceMap:   make(map[string]string),
    }
    p.AddToProcessorFunctionMap("init", &procFuncHsTestServiceInit{handler: handler})
    p.AddToFunctionServiceMap("init", "HsTestService")

    return p
}

func (p *HsTestServiceProcessor) AddToProcessorFunctionMap(key string, processorFunction thrift.ProcessorFunction) {
    p.processorFunctionMap[key] = processorFunction
}

func (p *HsTestServiceProcessor) AddToFunctionServiceMap(key, service string) {
    p.functionServiceMap[key] = service
}

func (p *HsTestServiceProcessor) GetProcessorFunction(key string) (processor thrift.ProcessorFunction) {
    return p.processorFunctionMap[key]
}

func (p *HsTestServiceProcessor) ProcessorFunctionMap() map[string]thrift.ProcessorFunction {
    return p.processorFunctionMap
}

func (p *HsTestServiceProcessor) FunctionServiceMap() map[string]string {
    return p.functionServiceMap
}

func (p *HsTestServiceProcessor) GetThriftMetadata() *metadata.ThriftMetadata {
    return GetThriftMetadataForService("hsmodule.HsTestService")
}


type procFuncHsTestServiceInit struct {
    handler HsTestService
}
// Compile time interface enforcer
var _ thrift.ProcessorFunction = (*procFuncHsTestServiceInit)(nil)

func (p *procFuncHsTestServiceInit) Read(iprot thrift.Decoder) (thrift.Struct, thrift.Exception) {
    args := newReqHsTestServiceInit()
    if err := args.Read(iprot); err != nil {
        return nil, err
    }
    iprot.ReadMessageEnd()
    return args, nil
}

func (p *procFuncHsTestServiceInit) Write(seqId int32, result thrift.WritableStruct, oprot thrift.Encoder) (err thrift.Exception) {
    var err2 error
    messageType := thrift.REPLY
    switch result.(type) {
    case thrift.ApplicationException:
        messageType = thrift.EXCEPTION
    }

    if err2 = oprot.WriteMessageBegin("init", messageType, seqId); err2 != nil {
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

func (p *procFuncHsTestServiceInit) RunContext(ctx context.Context, reqStruct thrift.Struct) (thrift.WritableStruct, thrift.ApplicationException) {
    args := reqStruct.(*reqHsTestServiceInit)
    result := newRespHsTestServiceInit()
    retval, err := p.handler.Init(ctx, args.Int1)
    if err != nil {
        x := thrift.NewApplicationExceptionCause(thrift.INTERNAL_ERROR, "Internal error processing Init: " + err.Error(), err)
        return x, x
    }

    result.Success = &retval
    return result, nil
}


