// Autogenerated by Thrift Compiler (facebook)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
// @generated

package rust

import (
	"bytes"
	"context"
	"sync"
	"fmt"
	thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift"
	scope0 "thrift/annotation/scope"

)

// (needed to ensure safety because of naive import list construction.)
var _ = thrift.ZERO
var _ = fmt.Printf
var _ = sync.Mutex{}
var _ = bytes.Equal
var _ = context.Background

var _ = scope0.GoUnusedProtection__
var GoUnusedProtection__ int;

// Attributes:
//  - Name
type Adapter struct {
  Name string `thrift:"name,1" db:"name" json:"name"`
}

func NewAdapter() *Adapter {
  return &Adapter{}
}


func (p *Adapter) GetName() string {
  return p.Name
}
type AdapterBuilder struct {
  obj *Adapter
}

func NewAdapterBuilder() *AdapterBuilder{
  return &AdapterBuilder{
    obj: NewAdapter(),
  }
}

func (p AdapterBuilder) Emit() *Adapter{
  return &Adapter{
    Name: p.obj.Name,
  }
}

func (a *AdapterBuilder) Name(name string) *AdapterBuilder {
  a.obj.Name = name
  return a
}

func (a *Adapter) SetName(name string) *Adapter {
  a.Name = name
  return a
}

func (p *Adapter) Read(iprot thrift.Protocol) error {
  if _, err := iprot.ReadStructBegin(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read error: ", p), err)
  }


  for {
    _, fieldTypeId, fieldId, err := iprot.ReadFieldBegin()
    if err != nil {
      return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", p, fieldId), err)
    }
    if fieldTypeId == thrift.STOP { break; }
    switch fieldId {
    case 1:
      if err := p.ReadField1(iprot); err != nil {
        return err
      }
    default:
      if err := iprot.Skip(fieldTypeId); err != nil {
        return err
      }
    }
    if err := iprot.ReadFieldEnd(); err != nil {
      return err
    }
  }
  if err := iprot.ReadStructEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", p), err)
  }
  return nil
}

func (p *Adapter)  ReadField1(iprot thrift.Protocol) error {
  if v, err := iprot.ReadString(); err != nil {
    return thrift.PrependError("error reading field 1: ", err)
  } else {
    p.Name = v
  }
  return nil
}

func (p *Adapter) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("Adapter"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *Adapter) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("name", thrift.STRING, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:name: ", p), err) }
  if err := oprot.WriteString(string(p.Name)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.name (1) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:name: ", p), err) }
  return err
}

func (p *Adapter) String() string {
  if p == nil {
    return "<nil>"
  }

  nameVal := fmt.Sprintf("%v", p.Name)
  return fmt.Sprintf("Adapter({Name:%s})", nameVal)
}

