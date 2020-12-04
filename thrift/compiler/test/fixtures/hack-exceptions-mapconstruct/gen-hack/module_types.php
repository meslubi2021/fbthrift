<?hh // strict
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

/**
 * Original thrift enum:-
 * MyEnum
 */
enum MyEnum: int as int {
  MyValue1 = 0;
  MyValue2 = 1;
}

/**
 * Original thrift exception:-
 * MyException1
 */
class MyException1 extends \TException implements \IThriftStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    1 => shape(
      'var' => 'message',
      'type' => \TType::STRING,
    ),
    2 => shape(
      'var' => 'code',
      'type' => \TType::I32,
      'enum' => MyEnum::class,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'message' => 1,
    'code' => 2,
  ];

  const type TConstructorShape = shape(
    ?'message' => ?string,
    ?'code' => ?MyEnum,
  );

  const int STRUCTURAL_ID = 7711048519845400283;
  /**
   * Original thrift field:-
   * 1: string message
   */
  public string $message;
  /**
   * Original thrift field:-
   * 2: enum module.MyEnum code
   */
  public /* Originally defined as MyEnum */ int $code;

  public function setCodeAsEnum(MyEnum $code): void {
    $this->code = $code;  
  }

  public function getCodeAsEnum(): MyEnum {
    /* HH_FIXME[4110] retain HHVM enforcement semantics */
    return $this->code;  
  }

  <<__Rx>>
  public function __construct(@KeyedContainer<string, mixed> $vals = dict[]) {
    parent::__construct();
    $this->message = (string)(idx($vals, 'message') ?? '');
    /* HH_FIXME[4110] exposed by decl fixme scope refinement */
    $this->code = idx($vals, 'code') ?? MyEnum::MyValue1;
  }

  <<__Rx>>
  public static function withDefaultValues(): this {
    return new static();
  }

  <<__Rx>>
  public static function fromShape(self::TConstructorShape $shape): this {
    return new static(
      Map {
        'message' => Shapes::idx($shape, 'message'),
        'code' => Shapes::idx($shape, 'code'),
      },
    );
  }

  <<__Rx>>
  public static function fromMap_DEPRECATED(@KeyedContainer<string, mixed> $map = dict[]): this {
    return new static($map);
  }

  public function getName(): string {
    return 'MyException1';
  }

  public static function getAllStructuredAnnotations(): \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
        'message' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
        'code' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
      ],
    );
  }

}

/**
 * Original thrift exception:-
 * MyException2
 */
class MyException2 extends \TException implements \IThriftStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    1 => shape(
      'var' => 'message',
      'type' => \TType::STRING,
    ),
    2 => shape(
      'var' => 'code',
      'type' => \TType::I32,
      'enum' => MyEnum::class,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'message' => 1,
    'code' => 2,
  ];

  const type TConstructorShape = shape(
    ?'message' => ?string,
    ?'code' => ?MyEnum,
  );

  const int STRUCTURAL_ID = 3067783023341493113;
  /**
   * Original thrift field:-
   * 1: string message
   */
  public string $message;
  /**
   * Original thrift field:-
   * 2: enum module.MyEnum code
   */
  public /* Originally defined as MyEnum */ int $code;

  public function setCodeAsEnum(MyEnum $code): void {
    $this->code = $code;  
  }

  public function getCodeAsEnum(): MyEnum {
    /* HH_FIXME[4110] retain HHVM enforcement semantics */
    return $this->code;  
  }

  <<__Rx>>
  public function __construct(@KeyedContainer<string, mixed> $vals = dict[]) {
    parent::__construct();
    $this->message = (string)(idx($vals, 'message') ?? '');
    /* HH_FIXME[4110] exposed by decl fixme scope refinement */
    $this->code = idx($vals, 'code') ?? MyEnum::MyValue1;
  }

  <<__Rx>>
  public static function withDefaultValues(): this {
    return new static();
  }

  <<__Rx>>
  public static function fromShape(self::TConstructorShape $shape): this {
    return new static(
      Map {
        'message' => Shapes::idx($shape, 'message'),
        'code' => Shapes::idx($shape, 'code'),
      },
    );
  }

  <<__Rx>>
  public static function fromMap_DEPRECATED(@KeyedContainer<string, mixed> $map = dict[]): this {
    return new static($map);
  }

  public function getName(): string {
    return 'MyException2';
  }

  public static function getAllStructuredAnnotations(): \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
        'message' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
        'code' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
      ],
    );
  }

}

/**
 * Original thrift exception:-
 * MyException3
 */
class MyException3 extends \TException implements \IThriftStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    1 => shape(
      'var' => 'message',
      'type' => \TType::STRING,
    ),
    2 => shape(
      'var' => 'code',
      'type' => \TType::I32,
      'enum' => MyEnum::class,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'message' => 1,
    'code' => 2,
  ];

  const type TConstructorShape = shape(
    ?'message' => ?string,
    ?'code' => ?MyEnum,
  );

  const int STRUCTURAL_ID = 3517193566312570591;
  /**
   * Original thrift field:-
   * 1: string message
   */
  public string $message;
  /**
   * Original thrift field:-
   * 2: enum module.MyEnum code
   */
  public /* Originally defined as MyEnum */ int $code;

  public function setCodeAsEnum(MyEnum $code): void {
    $this->code = $code;  
  }

  public function getCodeAsEnum(): MyEnum {
    /* HH_FIXME[4110] retain HHVM enforcement semantics */
    return $this->code;  
  }

  <<__Rx>>
  public function __construct(@KeyedContainer<string, mixed> $vals = dict[]) {
    parent::__construct();
    $this->message = (string)(idx($vals, 'message') ?? '');
    /* HH_FIXME[4110] exposed by decl fixme scope refinement */
    $this->code = idx($vals, 'code') ?? MyEnum::MyValue1;
  }

  <<__Rx>>
  public static function withDefaultValues(): this {
    return new static();
  }

  <<__Rx>>
  public static function fromShape(self::TConstructorShape $shape): this {
    return new static(
      Map {
        'message' => Shapes::idx($shape, 'message'),
        'code' => Shapes::idx($shape, 'code'),
      },
    );
  }

  <<__Rx>>
  public static function fromMap_DEPRECATED(@KeyedContainer<string, mixed> $map = dict[]): this {
    return new static($map);
  }

  public function getName(): string {
    return 'MyException3';
  }

  public static function getAllStructuredAnnotations(): \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
        'message' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
        'code' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
      ],
    );
  }

}

/**
 * Original thrift exception:-
 * MyException4
 */
class MyException4 extends \TException implements \IThriftStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    1 => shape(
      'var' => 'message',
      'type' => \TType::STRING,
    ),
    2 => shape(
      'var' => 'code',
      'type' => \TType::I32,
      'enum' => MyEnum::class,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'message' => 1,
    'code' => 2,
  ];

  const type TConstructorShape = shape(
    ?'message' => ?string,
    ?'code' => ?MyEnum,
  );

  const int STRUCTURAL_ID = 3517193566312570591;
  /**
   * Original thrift field:-
   * 1: string message
   */
  public string $message;
  /**
   * Original thrift field:-
   * 2: enum module.MyEnum code
   */
  public /* Originally defined as MyEnum */ int $code;

  public function setCodeAsEnum(MyEnum $code): void {
    $this->code = $code;  
  }

  public function getCodeAsEnum(): MyEnum {
    /* HH_FIXME[4110] retain HHVM enforcement semantics */
    return $this->code;  
  }

  <<__Rx>>
  public function __construct(@KeyedContainer<string, mixed> $vals = dict[]) {
    parent::__construct();
    $this->message = (string)(idx($vals, 'message') ?? '');
    /* HH_FIXME[4110] exposed by decl fixme scope refinement */
    $this->code = idx($vals, 'code') ?? MyEnum::MyValue2;
  }

  <<__Rx>>
  public static function withDefaultValues(): this {
    return new static();
  }

  <<__Rx>>
  public static function fromShape(self::TConstructorShape $shape): this {
    return new static(
      Map {
        'message' => Shapes::idx($shape, 'message'),
        'code' => Shapes::idx($shape, 'code'),
      },
    );
  }

  <<__Rx>>
  public static function fromMap_DEPRECATED(@KeyedContainer<string, mixed> $map = dict[]): this {
    return new static($map);
  }

  public function getName(): string {
    return 'MyException4';
  }

  public static function getAllStructuredAnnotations(): \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
        'message' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
        'code' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
      ],
    );
  }

}

/**
 * Original thrift exception:-
 * MyException5
 */
class MyException5 extends \TException implements \IThriftStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    1 => shape(
      'var' => 'message',
      'type' => \TType::STRING,
    ),
    2 => shape(
      'var' => 'code',
      'type' => \TType::I64,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'message' => 1,
    'code' => 2,
  ];

  const type TConstructorShape = shape(
    ?'message' => ?string,
    ?'code' => ?int,
  );

  const int STRUCTURAL_ID = 7335721753390449361;
  /**
   * Original thrift field:-
   * 1: string message
   */
  public string $message;
  /**
   * Original thrift field:-
   * 2: i64 code
   */
  public int $code;

  <<__Rx>>
  public function __construct(@KeyedContainer<string, mixed> $vals = dict[]) {
    parent::__construct();
    $this->message = (string)(idx($vals, 'message') ?? '');
    $this->code = (int)(idx($vals, 'code') ?? 0);
  }

  <<__Rx>>
  public static function withDefaultValues(): this {
    return new static();
  }

  <<__Rx>>
  public static function fromShape(self::TConstructorShape $shape): this {
    return new static(
      Map {
        'message' => Shapes::idx($shape, 'message'),
        'code' => Shapes::idx($shape, 'code'),
      },
    );
  }

  <<__Rx>>
  public static function fromMap_DEPRECATED(@KeyedContainer<string, mixed> $map = dict[]): this {
    return new static($map);
  }

  public function getName(): string {
    return 'MyException5';
  }

  public static function getAllStructuredAnnotations(): \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
        'message' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
        'code' => shape(
          'field' => dict[],
          'type' => dict[],
        ),
      ],
    );
  }

}

