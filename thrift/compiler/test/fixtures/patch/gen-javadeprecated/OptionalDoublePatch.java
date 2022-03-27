/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
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
public class OptionalDoublePatch implements TBase, java.io.Serializable, Cloneable, Comparable<OptionalDoublePatch> {
  private static final TStruct STRUCT_DESC = new TStruct("OptionalDoublePatch");
  private static final TField CLEAR_FIELD_DESC = new TField("clear", TType.BOOL, (short)2);
  private static final TField PATCH_FIELD_DESC = new TField("patch", TType.STRUCT, (short)3);
  private static final TField ENSURE_FIELD_DESC = new TField("ensure", TType.DOUBLE, (short)1);
  private static final TField PATCH_AFTER_FIELD_DESC = new TField("patchAfter", TType.STRUCT, (short)4);

  /**
   * Clears any set value. Applies first.
   */
  public boolean clear;
  /**
   * Patches any set value. Applies second.
   */
  public DoublePatch patch;
  /**
   * Initializes any unset value. Applies third.
   */
  public double ensure;
  /**
   * Patches any set value, including newly set values. Applies fourth.
   */
  public DoublePatch patchAfter;
  public static final int CLEAR = 2;
  public static final int PATCH = 3;
  public static final int ENSURE = 1;
  public static final int PATCHAFTER = 4;

  // isset id assignments
  private static final int __CLEAR_ISSET_ID = 0;
  private static final int __ENSURE_ISSET_ID = 1;
  private BitSet __isset_bit_vector = new BitSet(2);

  public static final Map<Integer, FieldMetaData> metaDataMap;

  static {
    Map<Integer, FieldMetaData> tmpMetaDataMap = new HashMap<Integer, FieldMetaData>();
    tmpMetaDataMap.put(CLEAR, new FieldMetaData("clear", TFieldRequirementType.DEFAULT, 
        new FieldValueMetaData(TType.BOOL)));
    tmpMetaDataMap.put(PATCH, new FieldMetaData("patch", TFieldRequirementType.DEFAULT, 
        new StructMetaData(TType.STRUCT, DoublePatch.class)));
    tmpMetaDataMap.put(ENSURE, new FieldMetaData("ensure", TFieldRequirementType.OPTIONAL, 
        new FieldValueMetaData(TType.DOUBLE)));
    tmpMetaDataMap.put(PATCHAFTER, new FieldMetaData("patchAfter", TFieldRequirementType.DEFAULT, 
        new StructMetaData(TType.STRUCT, DoublePatch.class)));
    metaDataMap = Collections.unmodifiableMap(tmpMetaDataMap);
  }

  static {
    FieldMetaData.addStructMetaDataMap(OptionalDoublePatch.class, metaDataMap);
  }

  public OptionalDoublePatch() {
  }

  public OptionalDoublePatch(
      boolean clear,
      DoublePatch patch,
      DoublePatch patchAfter) {
    this();
    this.clear = clear;
    setClearIsSet(true);
    this.patch = patch;
    this.patchAfter = patchAfter;
  }

  public OptionalDoublePatch(
      boolean clear,
      DoublePatch patch,
      double ensure,
      DoublePatch patchAfter) {
    this();
    this.clear = clear;
    setClearIsSet(true);
    this.patch = patch;
    this.ensure = ensure;
    setEnsureIsSet(true);
    this.patchAfter = patchAfter;
  }

  public static class Builder {
    private boolean clear;
    private DoublePatch patch;
    private double ensure;
    private DoublePatch patchAfter;

    BitSet __optional_isset = new BitSet(2);

    public Builder() {
    }

    public Builder setClear(final boolean clear) {
      this.clear = clear;
      __optional_isset.set(__CLEAR_ISSET_ID, true);
      return this;
    }

    public Builder setPatch(final DoublePatch patch) {
      this.patch = patch;
      return this;
    }

    public Builder setEnsure(final double ensure) {
      this.ensure = ensure;
      __optional_isset.set(__ENSURE_ISSET_ID, true);
      return this;
    }

    public Builder setPatchAfter(final DoublePatch patchAfter) {
      this.patchAfter = patchAfter;
      return this;
    }

    public OptionalDoublePatch build() {
      OptionalDoublePatch result = new OptionalDoublePatch();
      if (__optional_isset.get(__CLEAR_ISSET_ID)) {
        result.setClear(this.clear);
      }
      result.setPatch(this.patch);
      if (__optional_isset.get(__ENSURE_ISSET_ID)) {
        result.setEnsure(this.ensure);
      }
      result.setPatchAfter(this.patchAfter);
      return result;
    }
  }

  public static Builder builder() {
    return new Builder();
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public OptionalDoublePatch(OptionalDoublePatch other) {
    __isset_bit_vector.clear();
    __isset_bit_vector.or(other.__isset_bit_vector);
    this.clear = TBaseHelper.deepCopy(other.clear);
    if (other.isSetPatch()) {
      this.patch = TBaseHelper.deepCopy(other.patch);
    }
    this.ensure = TBaseHelper.deepCopy(other.ensure);
    if (other.isSetPatchAfter()) {
      this.patchAfter = TBaseHelper.deepCopy(other.patchAfter);
    }
  }

  public OptionalDoublePatch deepCopy() {
    return new OptionalDoublePatch(this);
  }

  /**
   * Clears any set value. Applies first.
   */
  public boolean isClear() {
    return this.clear;
  }

  /**
   * Clears any set value. Applies first.
   */
  public OptionalDoublePatch setClear(boolean clear) {
    this.clear = clear;
    setClearIsSet(true);
    return this;
  }

  public void unsetClear() {
    __isset_bit_vector.clear(__CLEAR_ISSET_ID);
  }

  // Returns true if field clear is set (has been assigned a value) and false otherwise
  public boolean isSetClear() {
    return __isset_bit_vector.get(__CLEAR_ISSET_ID);
  }

  public void setClearIsSet(boolean __value) {
    __isset_bit_vector.set(__CLEAR_ISSET_ID, __value);
  }

  /**
   * Patches any set value. Applies second.
   */
  public DoublePatch getPatch() {
    return this.patch;
  }

  /**
   * Patches any set value. Applies second.
   */
  public OptionalDoublePatch setPatch(DoublePatch patch) {
    this.patch = patch;
    return this;
  }

  public void unsetPatch() {
    this.patch = null;
  }

  // Returns true if field patch is set (has been assigned a value) and false otherwise
  public boolean isSetPatch() {
    return this.patch != null;
  }

  public void setPatchIsSet(boolean __value) {
    if (!__value) {
      this.patch = null;
    }
  }

  /**
   * Initializes any unset value. Applies third.
   */
  public double getEnsure() {
    return this.ensure;
  }

  /**
   * Initializes any unset value. Applies third.
   */
  public OptionalDoublePatch setEnsure(double ensure) {
    this.ensure = ensure;
    setEnsureIsSet(true);
    return this;
  }

  public void unsetEnsure() {
    __isset_bit_vector.clear(__ENSURE_ISSET_ID);
  }

  // Returns true if field ensure is set (has been assigned a value) and false otherwise
  public boolean isSetEnsure() {
    return __isset_bit_vector.get(__ENSURE_ISSET_ID);
  }

  public void setEnsureIsSet(boolean __value) {
    __isset_bit_vector.set(__ENSURE_ISSET_ID, __value);
  }

  /**
   * Patches any set value, including newly set values. Applies fourth.
   */
  public DoublePatch getPatchAfter() {
    return this.patchAfter;
  }

  /**
   * Patches any set value, including newly set values. Applies fourth.
   */
  public OptionalDoublePatch setPatchAfter(DoublePatch patchAfter) {
    this.patchAfter = patchAfter;
    return this;
  }

  public void unsetPatchAfter() {
    this.patchAfter = null;
  }

  // Returns true if field patchAfter is set (has been assigned a value) and false otherwise
  public boolean isSetPatchAfter() {
    return this.patchAfter != null;
  }

  public void setPatchAfterIsSet(boolean __value) {
    if (!__value) {
      this.patchAfter = null;
    }
  }

  public void setFieldValue(int fieldID, Object __value) {
    switch (fieldID) {
    case CLEAR:
      if (__value == null) {
        unsetClear();
      } else {
        setClear((Boolean)__value);
      }
      break;

    case PATCH:
      if (__value == null) {
        unsetPatch();
      } else {
        setPatch((DoublePatch)__value);
      }
      break;

    case ENSURE:
      if (__value == null) {
        unsetEnsure();
      } else {
        setEnsure((Double)__value);
      }
      break;

    case PATCHAFTER:
      if (__value == null) {
        unsetPatchAfter();
      } else {
        setPatchAfter((DoublePatch)__value);
      }
      break;

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  public Object getFieldValue(int fieldID) {
    switch (fieldID) {
    case CLEAR:
      return new Boolean(isClear());

    case PATCH:
      return getPatch();

    case ENSURE:
      return new Double(getEnsure());

    case PATCHAFTER:
      return getPatchAfter();

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
    if (!(_that instanceof OptionalDoublePatch))
      return false;
    OptionalDoublePatch that = (OptionalDoublePatch)_that;

    if (!TBaseHelper.equalsNobinary(this.clear, that.clear)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetPatch(), that.isSetPatch(), this.patch, that.patch)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetEnsure(), that.isSetEnsure(), this.ensure, that.ensure)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetPatchAfter(), that.isSetPatchAfter(), this.patchAfter, that.patchAfter)) { return false; }

    return true;
  }

  @Override
  public int hashCode() {
    return Arrays.deepHashCode(new Object[] {clear, patch, ensure, patchAfter});
  }

  @Override
  public int compareTo(OptionalDoublePatch other) {
    if (other == null) {
      // See java.lang.Comparable docs
      throw new NullPointerException();
    }

    if (other == this) {
      return 0;
    }
    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetClear()).compareTo(other.isSetClear());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(clear, other.clear);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetPatch()).compareTo(other.isSetPatch());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(patch, other.patch);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetEnsure()).compareTo(other.isSetEnsure());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(ensure, other.ensure);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetPatchAfter()).compareTo(other.isSetPatchAfter());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(patchAfter, other.patchAfter);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    return 0;
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
        case CLEAR:
          if (__field.type == TType.BOOL) {
            this.clear = iprot.readBool();
            setClearIsSet(true);
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case PATCH:
          if (__field.type == TType.STRUCT) {
            this.patch = new DoublePatch();
            this.patch.read(iprot);
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case ENSURE:
          if (__field.type == TType.DOUBLE) {
            this.ensure = iprot.readDouble();
            setEnsureIsSet(true);
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case PATCHAFTER:
          if (__field.type == TType.STRUCT) {
            this.patchAfter = new DoublePatch();
            this.patchAfter.read(iprot);
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
    if (isSetEnsure()) {
      oprot.writeFieldBegin(ENSURE_FIELD_DESC);
      oprot.writeDouble(this.ensure);
      oprot.writeFieldEnd();
    }
    oprot.writeFieldBegin(CLEAR_FIELD_DESC);
    oprot.writeBool(this.clear);
    oprot.writeFieldEnd();
    if (this.patch != null) {
      oprot.writeFieldBegin(PATCH_FIELD_DESC);
      this.patch.write(oprot);
      oprot.writeFieldEnd();
    }
    if (this.patchAfter != null) {
      oprot.writeFieldBegin(PATCH_AFTER_FIELD_DESC);
      this.patchAfter.write(oprot);
      oprot.writeFieldEnd();
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
    StringBuilder sb = new StringBuilder("OptionalDoublePatch");
    sb.append(space);
    sb.append("(");
    sb.append(newLine);
    boolean first = true;

    sb.append(indentStr);
    sb.append("clear");
    sb.append(space);
    sb.append(":").append(space);
    sb.append(TBaseHelper.toString(this.isClear(), indent + 1, prettyPrint));
    first = false;
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("patch");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getPatch() == null) {
      sb.append("null");
    } else {
      sb.append(TBaseHelper.toString(this.getPatch(), indent + 1, prettyPrint));
    }
    first = false;
    if (isSetEnsure())
    {
      if (!first) sb.append("," + newLine);
      sb.append(indentStr);
      sb.append("ensure");
      sb.append(space);
      sb.append(":").append(space);
      sb.append(TBaseHelper.toString(this.getEnsure(), indent + 1, prettyPrint));
      first = false;
    }
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("patchAfter");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getPatchAfter() == null) {
      sb.append("null");
    } else {
      sb.append(TBaseHelper.toString(this.getPatchAfter(), indent + 1, prettyPrint));
    }
    first = false;
    sb.append(newLine + TBaseHelper.reduceIndent(indentStr));
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws TException {
    // check for required fields
  }

}

