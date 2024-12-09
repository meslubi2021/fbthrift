<?hh
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

namespace facebook\thrift\annotation\python;

/**
 * Hides in thrift-py3 only, not in thrift-python
 *
 * Original thrift struct:-
 * Py3Hidden
 */
<<\ThriftTypeInfo(shape('uri' => 'facebook.com/thrift/annotation/python/Py3Hidden'))>>
class Py3Hidden implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Py3Hidden';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "python.Py3Hidden",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
    return shape(
      'struct' => dict[
        '\facebook\thrift\annotation\Definition' => \facebook\thrift\annotation\Definition::fromShape(
          shape(
          )
        ),
      ],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

/**
 * Hides in thrift-py-deprecated only
 *
 * Original thrift struct:-
 * PyDeprecatedHidden
 */
<<\ThriftTypeInfo(shape('uri' => 'facebook.com/thrift/annotation/python/PyDeprecatedHidden'))>>
class PyDeprecatedHidden implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
    1 => shape(
      'var' => 'reason',
      'type' => \TType::STRING,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'reason' => 1,
  ];

  const type TConstructorShape = shape(
    ?'reason' => ?string,
  );

  const int STRUCTURAL_ID = 3707764047816594739;
  /**
   * Original thrift field:-
   * 1: string reason
   */
  public string $reason;

  public function __construct(?string $reason = null)[] {
    $this->reason = $reason ?? '';
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'reason'),
    );
  }

  public function getName()[]: string {
    return 'PyDeprecatedHidden';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "python.PyDeprecatedHidden",
        "fields" => vec[
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 1,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_STRING_TYPE,
                )
              ),
              "name" => "reason",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
    return shape(
      'struct' => dict[
        '\facebook\thrift\annotation\Field' => \facebook\thrift\annotation\Field::fromShape(
          shape(
          )
        ),
      ],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

/**
 * Original thrift struct:-
 * Flags
 */
<<\ThriftTypeInfo(shape('uri' => 'facebook.com/thrift/annotation/python/Flags'))>>
class Flags implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Flags';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "python.Flags",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
    return shape(
      'struct' => dict[
        '\facebook\thrift\annotation\Enum' => \facebook\thrift\annotation\Enum::fromShape(
          shape(
          )
        ),
      ],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

/**
 * Original thrift struct:-
 * Name
 */
<<\ThriftTypeInfo(shape('uri' => 'facebook.com/thrift/annotation/python/Name'))>>
class Name implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
    1 => shape(
      'var' => 'name',
      'type' => \TType::STRING,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'name' => 1,
  ];

  const type TConstructorShape = shape(
    ?'name' => ?string,
  );

  const int STRUCTURAL_ID = 2593878277785201336;
  /**
   * Original thrift field:-
   * 1: string name
   */
  public string $name;

  public function __construct(?string $name = null)[] {
    $this->name = $name ?? '';
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'name'),
    );
  }

  public function getName()[]: string {
    return 'Name';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "python.Name",
        "fields" => vec[
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 1,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_STRING_TYPE,
                )
              ),
              "name" => "name",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
    return shape(
      'struct' => dict[
        '\facebook\thrift\annotation\Definition' => \facebook\thrift\annotation\Definition::fromShape(
          shape(
          )
        ),
      ],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

/**
 * An annotation that applies a Python adapter to typedef or field, or directly on struct.
 * This completely replaces the underlying type of a thrift for a custom implementation and
 * uses the specified adapter to convert to and from the underlying Thrift type during (de)serialization.
 * 
 * Example 1:
 * 
 *   @python.Adapter{name = "my.module.DatetimeAdapter", typeHint = "datetime.datetime"}
 *   typedef i64 Datetime
 * 
 * Here the type 'Datetime' has the Python adapter `DatetimeAdapter`.
 * 
 * 
 * Example 2:
 * 
 *   struct User {
 *     @python.Adapter{name = "my.module.DatetimeAdapter", typeHint = "datetime.datetime"}
 *     1: i64 created_at;
 *   }
 * Here the field `created_at` has the Python adapter `DatetimeAdapter`.
 * 
 * 
 * Example 3:
 * 
 * 
 *   @python.Adapter{name = "my.module.AnotherAdapter", typeHint = "my.module.AdaptedFoo"}
 *   struct Foo {
 *     1: string bar;
 *   }
 * 
 * Here the struct `Foo` has the Python adapter `AnotherAdapter`.
 * 
 *
 * Original thrift struct:-
 * Adapter
 */
<<\ThriftTypeInfo(shape('uri' => 'facebook.com/thrift/annotation/python/Adapter'))>>
class Adapter implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
    1 => shape(
      'var' => 'name',
      'type' => \TType::STRING,
    ),
    2 => shape(
      'var' => 'typeHint',
      'type' => \TType::STRING,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'name' => 1,
    'typeHint' => 2,
  ];

  const type TConstructorShape = shape(
    ?'name' => ?string,
    ?'typeHint' => ?string,
  );

  const int STRUCTURAL_ID = 8465306397732997722;
  /**
   * Fully qualified name of a Python adapter class, which should inherit from thrift.python.adapter.Adapter
   * 
   * Original thrift field:-
   * 1: string name
   */
  public string $name;
  /**
   * Fully qualified type hint the above implementation adapts to.
   * If ending with "[]", it becomes a generic, and the unadapted type will be filled between the brackets.
   * 
   * Original thrift field:-
   * 2: string typeHint
   */
  public string $typeHint;

  public function __construct(?string $name = null, ?string $typeHint = null)[] {
    $this->name = $name ?? '';
    $this->typeHint = $typeHint ?? '';
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'name'),
      Shapes::idx($shape, 'typeHint'),
    );
  }

  public function getName()[]: string {
    return 'Adapter';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "python.Adapter",
        "fields" => vec[
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 1,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_STRING_TYPE,
                )
              ),
              "name" => "name",
            )
          ),
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 2,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_STRING_TYPE,
                )
              ),
              "name" => "typeHint",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
    return shape(
      'struct' => dict[
        '\facebook\thrift\annotation\Field' => \facebook\thrift\annotation\Field::fromShape(
          shape(
          )
        ),
        '\facebook\thrift\annotation\Typedef' => \facebook\thrift\annotation\Typedef::fromShape(
          shape(
          )
        ),
        '\facebook\thrift\annotation\Structured' => \facebook\thrift\annotation\Structured::fromShape(
          shape(
          )
        ),
      ],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

/**
 * Controls cpp <-> python FFI for a struct or union
 * By default, struct uses marshal C API unless cpp.Type or cpp.Adapter is present
 * on a field or a type
 * Use this annotation to opt-in struct to marshal in spite of cpp.Type or cpp.Adapter
 * Alternatively, use this struct with serialize = false to use serialization for FFI.
 *
 * Original thrift struct:-
 * UseCAPI
 */
<<\ThriftTypeInfo(shape('uri' => 'facebook.com/thrift/annotation/python/UseCAPI'))>>
class UseCAPI implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
    1 => shape(
      'var' => 'serialize',
      'type' => \TType::BOOL,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'serialize' => 1,
  ];

  const type TConstructorShape = shape(
    ?'serialize' => ?bool,
  );

  const int STRUCTURAL_ID = 1251623031795142618;
  /**
   * Original thrift field:-
   * 1: bool serialize
   */
  public bool $serialize;

  public function __construct(?bool $serialize = null)[] {
    $this->serialize = $serialize ?? false;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'serialize'),
    );
  }

  public function getName()[]: string {
    return 'UseCAPI';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "python.UseCAPI",
        "fields" => vec[
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 1,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_BOOL_TYPE,
                )
              ),
              "name" => "serialize",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
    return shape(
      'struct' => dict[
        '\facebook\thrift\annotation\Structured' => \facebook\thrift\annotation\Structured::fromShape(
          shape(
          )
        ),
      ],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

/**
 * Enables C++ Adapter for thrift-py3. It treats C++ Adapter on typedef as cpp.Type.
 * It is only available for typedefs that resolve to binary, string, and container type.
 *
 * Original thrift struct:-
 * Py3EnableCppAdapter
 */
<<\ThriftTypeInfo(shape('uri' => 'facebook.com/thrift/annotation/python/Py3EnableCppAdapter'))>>
class Py3EnableCppAdapter implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Py3EnableCppAdapter';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "python.Py3EnableCppAdapter",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
    return shape(
      'struct' => dict[
        '\facebook\thrift\annotation\Typedef' => \facebook\thrift\annotation\Typedef::fromShape(
          shape(
          )
        ),
      ],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

