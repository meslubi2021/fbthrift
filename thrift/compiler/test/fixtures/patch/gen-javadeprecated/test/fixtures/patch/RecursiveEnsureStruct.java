/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package test.fixtures.patch;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;
import java.util.BitSet;
import java.util.Arrays;
import com.facebook.thrift.*;
import com.facebook.thrift.annotations.*;
import com.facebook.thrift.async.*;
import com.facebook.thrift.meta_data.*;
import com.facebook.thrift.server.*;
import com.facebook.thrift.transport.*;
import com.facebook.thrift.protocol.*;

@SuppressWarnings({ "unused", "serial" })
public class RecursiveEnsureStruct implements TBase, java.io.Serializable, Cloneable {
  private static final TStruct STRUCT_DESC = new TStruct("RecursiveEnsureStruct");
  private static final TField NODES_FIELD_DESC = new TField("nodes", TType.MAP, (short)-1);

  public Map<String,Recursive> nodes;
  public static final int NODES = -1;

  // isset id assignments

  public static final Map<Integer, FieldMetaData> metaDataMap;

  static {
    Map<Integer, FieldMetaData> tmpMetaDataMap = new HashMap<Integer, FieldMetaData>();
    tmpMetaDataMap.put(NODES, new FieldMetaData("nodes", TFieldRequirementType.OPTIONAL, 
        new MapMetaData(TType.MAP, 
            new FieldValueMetaData(TType.STRING), 
            new StructMetaData(TType.STRUCT, Recursive.class))));
    metaDataMap = Collections.unmodifiableMap(tmpMetaDataMap);
  }

  static {
    FieldMetaData.addStructMetaDataMap(RecursiveEnsureStruct.class, metaDataMap);
  }

  public RecursiveEnsureStruct() {
  }

  public RecursiveEnsureStruct(
      Map<String,Recursive> nodes) {
    this();
    this.nodes = nodes;
  }

  public static class Builder {
    private Map<String,Recursive> nodes;

    public Builder() {
    }

    public Builder setNodes(final Map<String,Recursive> nodes) {
      this.nodes = nodes;
      return this;
    }

    public RecursiveEnsureStruct build() {
      RecursiveEnsureStruct result = new RecursiveEnsureStruct();
      result.setNodes(this.nodes);
      return result;
    }
  }

  public static Builder builder() {
    return new Builder();
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public RecursiveEnsureStruct(RecursiveEnsureStruct other) {
    if (other.isSetNodes()) {
      this.nodes = TBaseHelper.deepCopy(other.nodes);
    }
  }

  public RecursiveEnsureStruct deepCopy() {
    return new RecursiveEnsureStruct(this);
  }

  public Map<String,Recursive> getNodes() {
    return this.nodes;
  }

  public RecursiveEnsureStruct setNodes(Map<String,Recursive> nodes) {
    this.nodes = nodes;
    return this;
  }

  public void unsetNodes() {
    this.nodes = null;
  }

  // Returns true if field nodes is set (has been assigned a value) and false otherwise
  public boolean isSetNodes() {
    return this.nodes != null;
  }

  public void setNodesIsSet(boolean __value) {
    if (!__value) {
      this.nodes = null;
    }
  }

  @SuppressWarnings("unchecked")
  public void setFieldValue(int fieldID, Object __value) {
    switch (fieldID) {
    case NODES:
      if (__value == null) {
        unsetNodes();
      } else {
        setNodes((Map<String,Recursive>)__value);
      }
      break;

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  public Object getFieldValue(int fieldID) {
    switch (fieldID) {
    case NODES:
      return getNodes();

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  @Override
  public boolean equals(Object _that) {
    if (_that == null)
      return false;
    if (this == _that)
      return true;
    if (!(_that instanceof RecursiveEnsureStruct))
      return false;
    RecursiveEnsureStruct that = (RecursiveEnsureStruct)_that;

    if (!TBaseHelper.equalsNobinary(this.isSetNodes(), that.isSetNodes(), this.nodes, that.nodes)) { return false; }

    return true;
  }

  @Override
  public int hashCode() {
    return Arrays.deepHashCode(new Object[] {nodes});
  }

  public void read(TProtocol iprot) throws TException {
    TField __field;
    iprot.readStructBegin(metaDataMap);
    while (true)
    {
      __field = iprot.readFieldBegin();
      if (__field.type == TType.STOP) {
        break;
      }
      switch (__field.id)
      {
        case NODES:
          if (__field.type == TType.MAP) {
            {
              TMap _map286 = iprot.readMapBegin();
              this.nodes = new HashMap<String,Recursive>(Math.max(0, 2*_map286.size));
              for (int _i287 = 0; 
                   (_map286.size < 0) ? iprot.peekMap() : (_i287 < _map286.size); 
                   ++_i287)
              {
                String _key288;
                Recursive _val289;
                _key288 = iprot.readString();
                _val289 = new Recursive();
                _val289.read(iprot);
                this.nodes.put(_key288, _val289);
              }
              iprot.readMapEnd();
            }
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        default:
          TProtocolUtil.skip(iprot, __field.type);
          break;
      }
      iprot.readFieldEnd();
    }
    iprot.readStructEnd();


    // check for required fields of primitive type, which can't be checked in the validate method
    validate();
  }

  public void write(TProtocol oprot) throws TException {
    validate();

    oprot.writeStructBegin(STRUCT_DESC);
    if (this.nodes != null) {
      if (isSetNodes()) {
        oprot.writeFieldBegin(NODES_FIELD_DESC);
        {
          oprot.writeMapBegin(new TMap(TType.STRING, TType.STRUCT, this.nodes.size()));
          for (Map.Entry<String, Recursive> _iter290 : this.nodes.entrySet())          {
            oprot.writeString(_iter290.getKey());
            _iter290.getValue().write(oprot);
          }
          oprot.writeMapEnd();
        }
        oprot.writeFieldEnd();
      }
    }
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  @Override
  public String toString() {
    return toString(1, true);
  }

  @Override
  public String toString(int indent, boolean prettyPrint) {
    String indentStr = prettyPrint ? TBaseHelper.getIndentedString(indent) : "";
    String newLine = prettyPrint ? "\n" : "";
    String space = prettyPrint ? " " : "";
    StringBuilder sb = new StringBuilder("RecursiveEnsureStruct");
    sb.append(space);
    sb.append("(");
    sb.append(newLine);
    boolean first = true;

    if (isSetNodes())
    {
      sb.append(indentStr);
      sb.append("nodes");
      sb.append(space);
      sb.append(":").append(space);
      if (this.getNodes() == null) {
        sb.append("null");
      } else {
        sb.append(TBaseHelper.toString(this.getNodes(), indent + 1, prettyPrint));
      }
      first = false;
    }
    sb.append(newLine + TBaseHelper.reduceIndent(indentStr));
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws TException {
    // check for required fields
  }

}

