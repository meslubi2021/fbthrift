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
public class MyStructField30Patch implements TBase, java.io.Serializable, Cloneable, Comparable<MyStructField30Patch> {
  private static final TStruct STRUCT_DESC = new TStruct("MyStructField30Patch");
  private static final TField ASSIGN_FIELD_DESC = new TField("assign", TType.MAP, (short)1);
  private static final TField CLEAR_FIELD_DESC = new TField("clear", TType.BOOL, (short)2);
  private static final TField PATCH_PRIOR_FIELD_DESC = new TField("patchPrior", TType.MAP, (short)3);
  private static final TField ADD_FIELD_DESC = new TField("add", TType.MAP, (short)5);
  private static final TField PATCH_FIELD_DESC = new TField("patch", TType.MAP, (short)6);
  private static final TField REMOVE_FIELD_DESC = new TField("remove", TType.SET, (short)7);
  private static final TField PUT_FIELD_DESC = new TField("put", TType.MAP, (short)9);

  /**
   * Assigns to a (set) value.
   * 
   * If set, all other operations are ignored.
   * 
   * Note: Optional and union fields must be set before assigned.
   * 
   */
  public Map<String,Map<String,Integer>> assign;
  /**
   * Clears a value. Applies first.
   */
  public boolean clear;
  /**
   * Patches any previously set values. Applies second.
   */
  public Map<String,MyStructField30Patch1> patchPrior;
  /**
   * Add the given values, if the keys are not already present. Applies forth.
   */
  public Map<String,Map<String,Integer>> add;
  /**
   * Patches any set value, including newly set values. Applies last.
   */
  public Map<String,MyStructField30Patch1> patch;
  /**
   * Removes entries, if present. Applies third.
   */
  public Set<String> remove;
  /**
   * Adds or replaces the given key/value pairs. Applies fifth.
   */
  public Map<String,Map<String,Integer>> put;
  public static final int ASSIGN = 1;
  public static final int CLEAR = 2;
  public static final int PATCHPRIOR = 3;
  public static final int ADD = 5;
  public static final int PATCH = 6;
  public static final int REMOVE = 7;
  public static final int PUT = 9;

  // isset id assignments
  private static final int __CLEAR_ISSET_ID = 0;
  private BitSet __isset_bit_vector = new BitSet(1);

  public static final Map<Integer, FieldMetaData> metaDataMap;

  static {
    Map<Integer, FieldMetaData> tmpMetaDataMap = new HashMap<Integer, FieldMetaData>();
    tmpMetaDataMap.put(ASSIGN, new FieldMetaData("assign", TFieldRequirementType.OPTIONAL, 
        new MapMetaData(TType.MAP, 
            new FieldValueMetaData(TType.STRING), 
            new MapMetaData(TType.MAP, 
                new FieldValueMetaData(TType.STRING), 
                new FieldValueMetaData(TType.I32)))));
    tmpMetaDataMap.put(CLEAR, new FieldMetaData("clear", TFieldRequirementType.DEFAULT, 
        new FieldValueMetaData(TType.BOOL)));
    tmpMetaDataMap.put(PATCHPRIOR, new FieldMetaData("patchPrior", TFieldRequirementType.DEFAULT, 
        new MapMetaData(TType.MAP, 
            new FieldValueMetaData(TType.STRING), 
            new StructMetaData(TType.STRUCT, MyStructField30Patch1.class))));
    tmpMetaDataMap.put(ADD, new FieldMetaData("add", TFieldRequirementType.DEFAULT, 
        new MapMetaData(TType.MAP, 
            new FieldValueMetaData(TType.STRING), 
            new MapMetaData(TType.MAP, 
                new FieldValueMetaData(TType.STRING), 
                new FieldValueMetaData(TType.I32)))));
    tmpMetaDataMap.put(PATCH, new FieldMetaData("patch", TFieldRequirementType.DEFAULT, 
        new MapMetaData(TType.MAP, 
            new FieldValueMetaData(TType.STRING), 
            new StructMetaData(TType.STRUCT, MyStructField30Patch1.class))));
    tmpMetaDataMap.put(REMOVE, new FieldMetaData("remove", TFieldRequirementType.DEFAULT, 
        new SetMetaData(TType.SET, 
            new FieldValueMetaData(TType.STRING))));
    tmpMetaDataMap.put(PUT, new FieldMetaData("put", TFieldRequirementType.DEFAULT, 
        new MapMetaData(TType.MAP, 
            new FieldValueMetaData(TType.STRING), 
            new MapMetaData(TType.MAP, 
                new FieldValueMetaData(TType.STRING), 
                new FieldValueMetaData(TType.I32)))));
    metaDataMap = Collections.unmodifiableMap(tmpMetaDataMap);
  }

  static {
    FieldMetaData.addStructMetaDataMap(MyStructField30Patch.class, metaDataMap);
  }

  public MyStructField30Patch() {
  }

  public MyStructField30Patch(
      boolean clear,
      Map<String,MyStructField30Patch1> patchPrior,
      Map<String,Map<String,Integer>> add,
      Map<String,MyStructField30Patch1> patch,
      Set<String> remove,
      Map<String,Map<String,Integer>> put) {
    this();
    this.clear = clear;
    setClearIsSet(true);
    this.patchPrior = patchPrior;
    this.add = add;
    this.patch = patch;
    this.remove = remove;
    this.put = put;
  }

  public MyStructField30Patch(
      Map<String,Map<String,Integer>> assign,
      boolean clear,
      Map<String,MyStructField30Patch1> patchPrior,
      Map<String,Map<String,Integer>> add,
      Map<String,MyStructField30Patch1> patch,
      Set<String> remove,
      Map<String,Map<String,Integer>> put) {
    this();
    this.assign = assign;
    this.clear = clear;
    setClearIsSet(true);
    this.patchPrior = patchPrior;
    this.add = add;
    this.patch = patch;
    this.remove = remove;
    this.put = put;
  }

  public static class Builder {
    private Map<String,Map<String,Integer>> assign;
    private boolean clear;
    private Map<String,MyStructField30Patch1> patchPrior;
    private Map<String,Map<String,Integer>> add;
    private Map<String,MyStructField30Patch1> patch;
    private Set<String> remove;
    private Map<String,Map<String,Integer>> put;

    BitSet __optional_isset = new BitSet(1);

    public Builder() {
    }

    public Builder setAssign(final Map<String,Map<String,Integer>> assign) {
      this.assign = assign;
      return this;
    }

    public Builder setClear(final boolean clear) {
      this.clear = clear;
      __optional_isset.set(__CLEAR_ISSET_ID, true);
      return this;
    }

    public Builder setPatchPrior(final Map<String,MyStructField30Patch1> patchPrior) {
      this.patchPrior = patchPrior;
      return this;
    }

    public Builder setAdd(final Map<String,Map<String,Integer>> add) {
      this.add = add;
      return this;
    }

    public Builder setPatch(final Map<String,MyStructField30Patch1> patch) {
      this.patch = patch;
      return this;
    }

    public Builder setRemove(final Set<String> remove) {
      this.remove = remove;
      return this;
    }

    public Builder setPut(final Map<String,Map<String,Integer>> put) {
      this.put = put;
      return this;
    }

    public MyStructField30Patch build() {
      MyStructField30Patch result = new MyStructField30Patch();
      result.setAssign(this.assign);
      if (__optional_isset.get(__CLEAR_ISSET_ID)) {
        result.setClear(this.clear);
      }
      result.setPatchPrior(this.patchPrior);
      result.setAdd(this.add);
      result.setPatch(this.patch);
      result.setRemove(this.remove);
      result.setPut(this.put);
      return result;
    }
  }

  public static Builder builder() {
    return new Builder();
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public MyStructField30Patch(MyStructField30Patch other) {
    __isset_bit_vector.clear();
    __isset_bit_vector.or(other.__isset_bit_vector);
    if (other.isSetAssign()) {
      this.assign = TBaseHelper.deepCopy(other.assign);
    }
    this.clear = TBaseHelper.deepCopy(other.clear);
    if (other.isSetPatchPrior()) {
      this.patchPrior = TBaseHelper.deepCopy(other.patchPrior);
    }
    if (other.isSetAdd()) {
      this.add = TBaseHelper.deepCopy(other.add);
    }
    if (other.isSetPatch()) {
      this.patch = TBaseHelper.deepCopy(other.patch);
    }
    if (other.isSetRemove()) {
      this.remove = TBaseHelper.deepCopy(other.remove);
    }
    if (other.isSetPut()) {
      this.put = TBaseHelper.deepCopy(other.put);
    }
  }

  public MyStructField30Patch deepCopy() {
    return new MyStructField30Patch(this);
  }

  /**
   * Assigns to a (set) value.
   * 
   * If set, all other operations are ignored.
   * 
   * Note: Optional and union fields must be set before assigned.
   * 
   */
  public Map<String,Map<String,Integer>> getAssign() {
    return this.assign;
  }

  /**
   * Assigns to a (set) value.
   * 
   * If set, all other operations are ignored.
   * 
   * Note: Optional and union fields must be set before assigned.
   * 
   */
  public MyStructField30Patch setAssign(Map<String,Map<String,Integer>> assign) {
    this.assign = assign;
    return this;
  }

  public void unsetAssign() {
    this.assign = null;
  }

  // Returns true if field assign is set (has been assigned a value) and false otherwise
  public boolean isSetAssign() {
    return this.assign != null;
  }

  public void setAssignIsSet(boolean __value) {
    if (!__value) {
      this.assign = null;
    }
  }

  /**
   * Clears a value. Applies first.
   */
  public boolean isClear() {
    return this.clear;
  }

  /**
   * Clears a value. Applies first.
   */
  public MyStructField30Patch setClear(boolean clear) {
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
   * Patches any previously set values. Applies second.
   */
  public Map<String,MyStructField30Patch1> getPatchPrior() {
    return this.patchPrior;
  }

  /**
   * Patches any previously set values. Applies second.
   */
  public MyStructField30Patch setPatchPrior(Map<String,MyStructField30Patch1> patchPrior) {
    this.patchPrior = patchPrior;
    return this;
  }

  public void unsetPatchPrior() {
    this.patchPrior = null;
  }

  // Returns true if field patchPrior is set (has been assigned a value) and false otherwise
  public boolean isSetPatchPrior() {
    return this.patchPrior != null;
  }

  public void setPatchPriorIsSet(boolean __value) {
    if (!__value) {
      this.patchPrior = null;
    }
  }

  /**
   * Add the given values, if the keys are not already present. Applies forth.
   */
  public Map<String,Map<String,Integer>> getAdd() {
    return this.add;
  }

  /**
   * Add the given values, if the keys are not already present. Applies forth.
   */
  public MyStructField30Patch setAdd(Map<String,Map<String,Integer>> add) {
    this.add = add;
    return this;
  }

  public void unsetAdd() {
    this.add = null;
  }

  // Returns true if field add is set (has been assigned a value) and false otherwise
  public boolean isSetAdd() {
    return this.add != null;
  }

  public void setAddIsSet(boolean __value) {
    if (!__value) {
      this.add = null;
    }
  }

  /**
   * Patches any set value, including newly set values. Applies last.
   */
  public Map<String,MyStructField30Patch1> getPatch() {
    return this.patch;
  }

  /**
   * Patches any set value, including newly set values. Applies last.
   */
  public MyStructField30Patch setPatch(Map<String,MyStructField30Patch1> patch) {
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
   * Removes entries, if present. Applies third.
   */
  public Set<String> getRemove() {
    return this.remove;
  }

  /**
   * Removes entries, if present. Applies third.
   */
  public MyStructField30Patch setRemove(Set<String> remove) {
    this.remove = remove;
    return this;
  }

  public void unsetRemove() {
    this.remove = null;
  }

  // Returns true if field remove is set (has been assigned a value) and false otherwise
  public boolean isSetRemove() {
    return this.remove != null;
  }

  public void setRemoveIsSet(boolean __value) {
    if (!__value) {
      this.remove = null;
    }
  }

  /**
   * Adds or replaces the given key/value pairs. Applies fifth.
   */
  public Map<String,Map<String,Integer>> getPut() {
    return this.put;
  }

  /**
   * Adds or replaces the given key/value pairs. Applies fifth.
   */
  public MyStructField30Patch setPut(Map<String,Map<String,Integer>> put) {
    this.put = put;
    return this;
  }

  public void unsetPut() {
    this.put = null;
  }

  // Returns true if field put is set (has been assigned a value) and false otherwise
  public boolean isSetPut() {
    return this.put != null;
  }

  public void setPutIsSet(boolean __value) {
    if (!__value) {
      this.put = null;
    }
  }

  @SuppressWarnings("unchecked")
  public void setFieldValue(int fieldID, Object __value) {
    switch (fieldID) {
    case ASSIGN:
      if (__value == null) {
        unsetAssign();
      } else {
        setAssign((Map<String,Map<String,Integer>>)__value);
      }
      break;

    case CLEAR:
      if (__value == null) {
        unsetClear();
      } else {
        setClear((Boolean)__value);
      }
      break;

    case PATCHPRIOR:
      if (__value == null) {
        unsetPatchPrior();
      } else {
        setPatchPrior((Map<String,MyStructField30Patch1>)__value);
      }
      break;

    case ADD:
      if (__value == null) {
        unsetAdd();
      } else {
        setAdd((Map<String,Map<String,Integer>>)__value);
      }
      break;

    case PATCH:
      if (__value == null) {
        unsetPatch();
      } else {
        setPatch((Map<String,MyStructField30Patch1>)__value);
      }
      break;

    case REMOVE:
      if (__value == null) {
        unsetRemove();
      } else {
        setRemove((Set<String>)__value);
      }
      break;

    case PUT:
      if (__value == null) {
        unsetPut();
      } else {
        setPut((Map<String,Map<String,Integer>>)__value);
      }
      break;

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  public Object getFieldValue(int fieldID) {
    switch (fieldID) {
    case ASSIGN:
      return getAssign();

    case CLEAR:
      return new Boolean(isClear());

    case PATCHPRIOR:
      return getPatchPrior();

    case ADD:
      return getAdd();

    case PATCH:
      return getPatch();

    case REMOVE:
      return getRemove();

    case PUT:
      return getPut();

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
    if (!(_that instanceof MyStructField30Patch))
      return false;
    MyStructField30Patch that = (MyStructField30Patch)_that;

    if (!TBaseHelper.equalsNobinary(this.isSetAssign(), that.isSetAssign(), this.assign, that.assign)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.clear, that.clear)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetPatchPrior(), that.isSetPatchPrior(), this.patchPrior, that.patchPrior)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetAdd(), that.isSetAdd(), this.add, that.add)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetPatch(), that.isSetPatch(), this.patch, that.patch)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetRemove(), that.isSetRemove(), this.remove, that.remove)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetPut(), that.isSetPut(), this.put, that.put)) { return false; }

    return true;
  }

  @Override
  public int hashCode() {
    return Arrays.deepHashCode(new Object[] {assign, clear, patchPrior, add, patch, remove, put});
  }

  @Override
  public int compareTo(MyStructField30Patch other) {
    if (other == null) {
      // See java.lang.Comparable docs
      throw new NullPointerException();
    }

    if (other == this) {
      return 0;
    }
    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetAssign()).compareTo(other.isSetAssign());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(assign, other.assign);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetClear()).compareTo(other.isSetClear());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(clear, other.clear);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetPatchPrior()).compareTo(other.isSetPatchPrior());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(patchPrior, other.patchPrior);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetAdd()).compareTo(other.isSetAdd());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(add, other.add);
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
    lastComparison = Boolean.valueOf(isSetRemove()).compareTo(other.isSetRemove());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(remove, other.remove);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetPut()).compareTo(other.isSetPut());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(put, other.put);
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
        case ASSIGN:
          if (__field.type == TType.MAP) {
            {
              TMap _map168 = iprot.readMapBegin();
              this.assign = new HashMap<String,Map<String,Integer>>(Math.max(0, 2*_map168.size));
              for (int _i169 = 0; 
                   (_map168.size < 0) ? iprot.peekMap() : (_i169 < _map168.size); 
                   ++_i169)
              {
                String _key170;
                Map<String,Integer> _val171;
                _key170 = iprot.readString();
                {
                  TMap _map172 = iprot.readMapBegin();
                  _val171 = new HashMap<String,Integer>(Math.max(0, 2*_map172.size));
                  for (int _i173 = 0; 
                       (_map172.size < 0) ? iprot.peekMap() : (_i173 < _map172.size); 
                       ++_i173)
                  {
                    String _key174;
                    int _val175;
                    _key174 = iprot.readString();
                    _val175 = iprot.readI32();
                    _val171.put(_key174, _val175);
                  }
                  iprot.readMapEnd();
                }
                this.assign.put(_key170, _val171);
              }
              iprot.readMapEnd();
            }
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case CLEAR:
          if (__field.type == TType.BOOL) {
            this.clear = iprot.readBool();
            setClearIsSet(true);
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case PATCHPRIOR:
          if (__field.type == TType.MAP) {
            {
              TMap _map176 = iprot.readMapBegin();
              this.patchPrior = new HashMap<String,MyStructField30Patch1>(Math.max(0, 2*_map176.size));
              for (int _i177 = 0; 
                   (_map176.size < 0) ? iprot.peekMap() : (_i177 < _map176.size); 
                   ++_i177)
              {
                String _key178;
                MyStructField30Patch1 _val179;
                _key178 = iprot.readString();
                _val179 = new MyStructField30Patch1();
                _val179.read(iprot);
                this.patchPrior.put(_key178, _val179);
              }
              iprot.readMapEnd();
            }
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case ADD:
          if (__field.type == TType.MAP) {
            {
              TMap _map180 = iprot.readMapBegin();
              this.add = new HashMap<String,Map<String,Integer>>(Math.max(0, 2*_map180.size));
              for (int _i181 = 0; 
                   (_map180.size < 0) ? iprot.peekMap() : (_i181 < _map180.size); 
                   ++_i181)
              {
                String _key182;
                Map<String,Integer> _val183;
                _key182 = iprot.readString();
                {
                  TMap _map184 = iprot.readMapBegin();
                  _val183 = new HashMap<String,Integer>(Math.max(0, 2*_map184.size));
                  for (int _i185 = 0; 
                       (_map184.size < 0) ? iprot.peekMap() : (_i185 < _map184.size); 
                       ++_i185)
                  {
                    String _key186;
                    int _val187;
                    _key186 = iprot.readString();
                    _val187 = iprot.readI32();
                    _val183.put(_key186, _val187);
                  }
                  iprot.readMapEnd();
                }
                this.add.put(_key182, _val183);
              }
              iprot.readMapEnd();
            }
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case PATCH:
          if (__field.type == TType.MAP) {
            {
              TMap _map188 = iprot.readMapBegin();
              this.patch = new HashMap<String,MyStructField30Patch1>(Math.max(0, 2*_map188.size));
              for (int _i189 = 0; 
                   (_map188.size < 0) ? iprot.peekMap() : (_i189 < _map188.size); 
                   ++_i189)
              {
                String _key190;
                MyStructField30Patch1 _val191;
                _key190 = iprot.readString();
                _val191 = new MyStructField30Patch1();
                _val191.read(iprot);
                this.patch.put(_key190, _val191);
              }
              iprot.readMapEnd();
            }
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case REMOVE:
          if (__field.type == TType.SET) {
            {
              TSet _set192 = iprot.readSetBegin();
              this.remove = new HashSet<String>(Math.max(0, 2*_set192.size));
              for (int _i193 = 0; 
                   (_set192.size < 0) ? iprot.peekSet() : (_i193 < _set192.size); 
                   ++_i193)
              {
                String _elem194;
                _elem194 = iprot.readString();
                this.remove.add(_elem194);
              }
              iprot.readSetEnd();
            }
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case PUT:
          if (__field.type == TType.MAP) {
            {
              TMap _map195 = iprot.readMapBegin();
              this.put = new HashMap<String,Map<String,Integer>>(Math.max(0, 2*_map195.size));
              for (int _i196 = 0; 
                   (_map195.size < 0) ? iprot.peekMap() : (_i196 < _map195.size); 
                   ++_i196)
              {
                String _key197;
                Map<String,Integer> _val198;
                _key197 = iprot.readString();
                {
                  TMap _map199 = iprot.readMapBegin();
                  _val198 = new HashMap<String,Integer>(Math.max(0, 2*_map199.size));
                  for (int _i200 = 0; 
                       (_map199.size < 0) ? iprot.peekMap() : (_i200 < _map199.size); 
                       ++_i200)
                  {
                    String _key201;
                    int _val202;
                    _key201 = iprot.readString();
                    _val202 = iprot.readI32();
                    _val198.put(_key201, _val202);
                  }
                  iprot.readMapEnd();
                }
                this.put.put(_key197, _val198);
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
    if (this.assign != null) {
      if (isSetAssign()) {
        oprot.writeFieldBegin(ASSIGN_FIELD_DESC);
        {
          oprot.writeMapBegin(new TMap(TType.STRING, TType.MAP, this.assign.size()));
          for (Map.Entry<String, Map<String,Integer>> _iter203 : this.assign.entrySet())          {
            oprot.writeString(_iter203.getKey());
            {
              oprot.writeMapBegin(new TMap(TType.STRING, TType.I32, _iter203.getValue().size()));
              for (Map.Entry<String, Integer> _iter204 : _iter203.getValue().entrySet())              {
                oprot.writeString(_iter204.getKey());
                oprot.writeI32(_iter204.getValue());
              }
              oprot.writeMapEnd();
            }
          }
          oprot.writeMapEnd();
        }
        oprot.writeFieldEnd();
      }
    }
    oprot.writeFieldBegin(CLEAR_FIELD_DESC);
    oprot.writeBool(this.clear);
    oprot.writeFieldEnd();
    if (this.patchPrior != null) {
      oprot.writeFieldBegin(PATCH_PRIOR_FIELD_DESC);
      {
        oprot.writeMapBegin(new TMap(TType.STRING, TType.STRUCT, this.patchPrior.size()));
        for (Map.Entry<String, MyStructField30Patch1> _iter205 : this.patchPrior.entrySet())        {
          oprot.writeString(_iter205.getKey());
          _iter205.getValue().write(oprot);
        }
        oprot.writeMapEnd();
      }
      oprot.writeFieldEnd();
    }
    if (this.add != null) {
      oprot.writeFieldBegin(ADD_FIELD_DESC);
      {
        oprot.writeMapBegin(new TMap(TType.STRING, TType.MAP, this.add.size()));
        for (Map.Entry<String, Map<String,Integer>> _iter206 : this.add.entrySet())        {
          oprot.writeString(_iter206.getKey());
          {
            oprot.writeMapBegin(new TMap(TType.STRING, TType.I32, _iter206.getValue().size()));
            for (Map.Entry<String, Integer> _iter207 : _iter206.getValue().entrySet())            {
              oprot.writeString(_iter207.getKey());
              oprot.writeI32(_iter207.getValue());
            }
            oprot.writeMapEnd();
          }
        }
        oprot.writeMapEnd();
      }
      oprot.writeFieldEnd();
    }
    if (this.patch != null) {
      oprot.writeFieldBegin(PATCH_FIELD_DESC);
      {
        oprot.writeMapBegin(new TMap(TType.STRING, TType.STRUCT, this.patch.size()));
        for (Map.Entry<String, MyStructField30Patch1> _iter208 : this.patch.entrySet())        {
          oprot.writeString(_iter208.getKey());
          _iter208.getValue().write(oprot);
        }
        oprot.writeMapEnd();
      }
      oprot.writeFieldEnd();
    }
    if (this.remove != null) {
      oprot.writeFieldBegin(REMOVE_FIELD_DESC);
      {
        oprot.writeSetBegin(new TSet(TType.STRING, this.remove.size()));
        for (String _iter209 : this.remove)        {
          oprot.writeString(_iter209);
        }
        oprot.writeSetEnd();
      }
      oprot.writeFieldEnd();
    }
    if (this.put != null) {
      oprot.writeFieldBegin(PUT_FIELD_DESC);
      {
        oprot.writeMapBegin(new TMap(TType.STRING, TType.MAP, this.put.size()));
        for (Map.Entry<String, Map<String,Integer>> _iter210 : this.put.entrySet())        {
          oprot.writeString(_iter210.getKey());
          {
            oprot.writeMapBegin(new TMap(TType.STRING, TType.I32, _iter210.getValue().size()));
            for (Map.Entry<String, Integer> _iter211 : _iter210.getValue().entrySet())            {
              oprot.writeString(_iter211.getKey());
              oprot.writeI32(_iter211.getValue());
            }
            oprot.writeMapEnd();
          }
        }
        oprot.writeMapEnd();
      }
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
    StringBuilder sb = new StringBuilder("MyStructField30Patch");
    sb.append(space);
    sb.append("(");
    sb.append(newLine);
    boolean first = true;

    if (isSetAssign())
    {
      sb.append(indentStr);
      sb.append("assign");
      sb.append(space);
      sb.append(":").append(space);
      if (this.getAssign() == null) {
        sb.append("null");
      } else {
        sb.append(TBaseHelper.toString(this.getAssign(), indent + 1, prettyPrint));
      }
      first = false;
    }
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("clear");
    sb.append(space);
    sb.append(":").append(space);
    sb.append(TBaseHelper.toString(this.isClear(), indent + 1, prettyPrint));
    first = false;
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("patchPrior");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getPatchPrior() == null) {
      sb.append("null");
    } else {
      sb.append(TBaseHelper.toString(this.getPatchPrior(), indent + 1, prettyPrint));
    }
    first = false;
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("add");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getAdd() == null) {
      sb.append("null");
    } else {
      sb.append(TBaseHelper.toString(this.getAdd(), indent + 1, prettyPrint));
    }
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
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("remove");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getRemove() == null) {
      sb.append("null");
    } else {
      sb.append(TBaseHelper.toString(this.getRemove(), indent + 1, prettyPrint));
    }
    first = false;
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("put");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getPut() == null) {
      sb.append("null");
    } else {
      sb.append(TBaseHelper.toString(this.getPut(), indent + 1, prettyPrint));
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

