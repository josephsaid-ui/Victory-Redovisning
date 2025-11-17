# TypeScript - Den Kompletta Guiden: Från Nybörjare till Expert

> Type-safe JavaScript - från grunden till produktion

---

## 📚 Innehållsförteckning

- [🎯 Om Denna Guide](#-om-denna-guide)
- [🤔 Vad är TypeScript?](#-vad-är-typescript)
- [Nivå 1: Varför Typer? 👶](#nivå-1-varför-typer-)
- [Nivå 2: Grundläggande TypeScript 🧒](#nivå-2-grundläggande-typescript-)
- [Nivå 3: Interfaces & Types 🎓](#nivå-3-interfaces--types-)
- [Nivå 4: Avancerade Typer 🚀](#nivå-4-avancerade-typer-)
- [Nivå 5: Expert Patterns 💎](#nivå-5-expert-patterns-)
- [🎓 Självutvärdering](#-självutvärdering)
- [📖 Ordlista](#-ordlista)
- [🆚 TypeScript vs JavaScript](#-typescript-vs-javascript)
- [🔗 Resurser](#-resurser)
- [❓ FAQ](#-faq)

---

## 🎯 Om Denna Guide

Lär dig TypeScript från grunden - JavaScript med superkrafter!

**5 nivåer:**
- 👶 **Nivå 1**: Varför typer? (koncept)
- 🧒 **Nivå 2**: Basic types & annotations
- 🎓 **Nivå 3**: Interfaces, types, generics
- 🚀 **Nivå 4**: Advanced types, utility types
- 💎 **Nivå 5**: Expert patterns, strict mode

**Läsningstid:** 1.5-2 timmar

---

## 🤔 Vad är TypeScript?

TypeScript = JavaScript + Types

```javascript
// JavaScript - Inga typer
function add(a, b) {
  return a + b
}

add(5, 3)      // 8 ✅
add('5', '3')  // '53' 😱 (string concatenation!)

// TypeScript - Med typer
function add(a: number, b: number): number {
  return a + b
}

add(5, 3)      // 8 ✅
add('5', '3')  // ERROR: strings inte allowed! 🛡️
```

**Fördelar:**
- ✅ Fånga buggar innan runtime
- ✅ Autocomplete i editor
- ✅ Bättre dokumentation
- ✅ Refactoring blir säkrare
- ✅ Skalbar kod

**Används av:**
- Microsoft, Google, Airbnb, Slack
- Nästan alla stora projekt
- React, Vue, Angular (alla stödjer TS)

---

## Nivå 1: Varför Typer? 👶

### Problemet med JavaScript

```javascript
// JavaScript - allt tillåts
let age = 25
age = "tjugofem"  // OK... men kanske inte vad vi ville?
age = true        // OK... men verkar fel?
age.toUpperCase() // Runtime ERROR! 💥
```

### Lösningen - TypeScript

```typescript
// TypeScript - säkerhet
let age: number = 25
age = "tjugofem"  // ERROR: Type 'string' is not assignable to 'number' ✋
age = true        // ERROR ✋

// Editorn hjälper dig:
age.toFixed(2)    // ✅ Autocomplete ger förslag!
```

### Analogier

**Tänk på en låda:**

**JavaScript:**
```
📦 Låda
- Kan innehålla: Äpplen, Böcker, Bilar, Vad som helst!
- Problem: Du vet inte vad som är i lådan förrän du öppnar den
```

**TypeScript:**
```
📦 Låda märkt "Äpplen"
- Kan BARA innehålla: Äpplen 🍎
- Fördel: Du vet exakt vad som är i lådan
- Säkerhet: Kan inte råka stoppa in en bil
```

---

## Nivå 2: Grundläggande TypeScript 🧒

### Primitive Types

```typescript
// Number
let age: number = 25
let price: number = 99.99

// String
let name: string = "Anna"
let greeting: string = 'Hej'

// Boolean
let isActive: boolean = true
let hasAccess: boolean = false

// Any (undvik!)
let anything: any = "whatever"
anything = 123
anything = true  // Any tillåter allt (dålig practice!)

// Unknown (bättre än any)
let something: unknown = "test"
// something.toUpperCase()  // ERROR
if (typeof something === 'string') {
  something.toUpperCase()  // OK nu! ✅
}
```

### Arrays & Tuples

```typescript
// Array
let numbers: number[] = [1, 2, 3]
let names: Array<string> = ['Anna', 'Erik']

// Tuple (fix längd och typer)
let person: [string, number] = ['Anna', 25]
person = ['Erik', 30]  // OK
person = [30, 'Erik']  // ERROR: fel ordning!
```

### Objects

```typescript
// Object type
let user: {
  name: string
  age: number
  email?: string  // ? = optional
} = {
  name: 'Anna',
  age: 25
  // email är optional, behövs inte
}

// Index signature
let scores: { [key: string]: number } = {
  math: 90,
  english: 85
}
```

### Functions

```typescript
// Function types
function add(a: number, b: number): number {
  return a + b
}

// Arrow function
const subtract = (a: number, b: number): number => a - b

// Optional parameters
function greet(name: string, greeting?: string): string {
  return `${greeting || 'Hej'} ${name}`
}

// Default parameters
function multiply(a: number, b: number = 2): number {
  return a * b
}

multiply(5)     // 10
multiply(5, 3)  // 15

// Rest parameters
function sum(...numbers: number[]): number {
  return numbers.reduce((total, n) => total + n, 0)
}
```

---

## Nivå 3: Interfaces & Types 🎓

### Interfaces

```typescript
// Interface för objekt
interface User {
  id: number
  name: string
  email: string
  age?: number  // optional
  readonly createdAt: Date  // kan inte ändras
}

const user: User = {
  id: 1,
  name: 'Anna',
  email: 'anna@example.com',
  createdAt: new Date()
}

// user.createdAt = new Date()  // ERROR: readonly!

// Extending interfaces
interface Admin extends User {
  role: 'admin' | 'superadmin'
  permissions: string[]
}

const admin: Admin = {
  id: 1,
  name: 'Admin',
  email: 'admin@example.com',
  createdAt: new Date(),
  role: 'admin',
  permissions: ['read', 'write']
}
```

### Type Aliases

```typescript
// Type alias
type ID = string | number

type User = {
  id: ID
  name: string
  email: string
}

// Union types
type Status = 'pending' | 'active' | 'inactive'
let status: Status = 'active'  // OK
// status = 'deleted'  // ERROR: not in union!

// Intersection types
type Timestamped = {
  createdAt: Date
  updatedAt: Date
}

type Product = {
  id: number
  name: string
  price: number
}

type TimestampedProduct = Product & Timestamped

const product: TimestampedProduct = {
  id: 1,
  name: 'Laptop',
  price: 999,
  createdAt: new Date(),
  updatedAt: new Date()
}
```

### Generics

```typescript
// Generic function
function identity<T>(value: T): T {
  return value
}

identity<number>(42)       // 42
identity<string>('hello')  // 'hello'
identity(true)             // type inferred: boolean

// Generic array function
function firstElement<T>(arr: T[]): T | undefined {
  return arr[0]
}

firstElement([1, 2, 3])           // number
firstElement(['a', 'b', 'c'])     // string

// Generic interface
interface Box<T> {
  value: T
}

const numberBox: Box<number> = { value: 42 }
const stringBox: Box<string> = { value: 'hello' }

// Multiple type parameters
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second]
}

pair(1, 'one')      // [number, string]
pair(true, [1, 2])  // [boolean, number[]]
```

### Type Guards

```typescript
// typeof guard
function process(value: string | number) {
  if (typeof value === 'string') {
    return value.toUpperCase()  // TS knows it's string
  } else {
    return value.toFixed(2)     // TS knows it's number
  }
}

// instanceof guard
class Dog {
  bark() { console.log('Woof!') }
}

class Cat {
  meow() { console.log('Meow!') }
}

function makeSound(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    animal.bark()  // TS knows it's Dog
  } else {
    animal.meow()  // TS knows it's Cat
  }
}

// Custom type guard
interface Fish {
  swim: () => void
}

interface Bird {
  fly: () => void
}

function isFish(animal: Fish | Bird): animal is Fish {
  return (animal as Fish).swim !== undefined
}

function move(animal: Fish | Bird) {
  if (isFish(animal)) {
    animal.swim()  // TS knows it's Fish
  } else {
    animal.fly()   // TS knows it's Bird
  }
}
```

---

## Nivå 4: Avancerade Typer 🚀

### Utility Types

```typescript
// Partial - gör alla properties optional
interface Todo {
  title: string
  description: string
  completed: boolean
}

function updateTodo(todo: Todo, fieldsToUpdate: Partial<Todo>) {
  return { ...todo, ...fieldsToUpdate }
}

// Required - gör alla properties required
type RequiredTodo = Required<Partial<Todo>>

// Readonly - gör alla properties readonly
type ReadonlyTodo = Readonly<Todo>

// Pick - välj vissa properties
type TodoPreview = Pick<Todo, 'title' | 'completed'>

// Omit - exkludera vissa properties
type TodoInfo = Omit<Todo, 'completed'>

// Record - skapa objekt type
type PageInfo = {
  title: string
}

type Pages = 'home' | 'about' | 'contact'
const pages: Record<Pages, PageInfo> = {
  home: { title: 'Home' },
  about: { title: 'About' },
  contact: { title: 'Contact' }
}

// ReturnType - få return type från funktion
function getUser() {
  return { id: 1, name: 'Anna' }
}

type User = ReturnType<typeof getUser>
// { id: number, name: string }
```

### Mapped Types

```typescript
type Readonly<T> = {
  readonly [P in keyof T]: T[P]
}

type Partial<T> = {
  [P in keyof T]?: T[P]
}

// Custom mapped type
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
}

interface Person {
  name: string
  age: number
}

type PersonGetters = Getters<Person>
// {
//   getName: () => string
//   getAge: () => number
// }
```

### Conditional Types

```typescript
type IsString<T> = T extends string ? true : false

type A = IsString<string>  // true
type B = IsString<number>  // false

// Extract - få union members som matchar
type T0 = Extract<'a' | 'b' | 'c', 'a' | 'f'>  // 'a'

// Exclude - ta bort union members
type T1 = Exclude<'a' | 'b' | 'c', 'a'>  // 'b' | 'c'

// NonNullable - ta bort null och undefined
type T2 = NonNullable<string | number | undefined>  // string | number
```

### Template Literal Types

```typescript
type World = 'world'
type Greeting = `hello ${World}`  // 'hello world'

type Color = 'red' | 'blue'
type Quantity = 'one' | 'two'
type SeussFish = `${Quantity | Color} fish`
// 'one fish' | 'two fish' | 'red fish' | 'blue fish'

// Event names
type PropEventSource<T> = {
  on<K extends string & keyof T>(
    eventName: `${K}Changed`,
    callback: (newValue: T[K]) => void
  ): void
}

declare function makeWatchedObject<T>(obj: T): T & PropEventSource<T>

const person = makeWatchedObject({
  firstName: 'Anna',
  age: 25
})

person.on('firstNameChanged', newName => {
  console.log(`Name changed to ${newName}`)
})
```

---

## Nivå 5: Expert Patterns 💎

### Strict Mode

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,  // Aktivera alla strict checks
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true
  }
}
```

### Discriminated Unions

```typescript
interface Square {
  kind: 'square'
  size: number
}

interface Rectangle {
  kind: 'rectangle'
  width: number
  height: number
}

interface Circle {
  kind: 'circle'
  radius: number
}

type Shape = Square | Rectangle | Circle

function area(shape: Shape): number {
  switch (shape.kind) {
    case 'square':
      return shape.size ** 2
    case 'rectangle':
      return shape.width * shape.height
    case 'circle':
      return Math.PI * shape.radius ** 2
  }
}
```

### Advanced Generics

```typescript
// Generic constraints
interface Lengthwise {
  length: number
}

function logLength<T extends Lengthwise>(arg: T): T {
  console.log(arg.length)
  return arg
}

logLength('hello')     // OK: string has length
logLength([1, 2, 3])   // OK: array has length
// logLength(3)        // ERROR: number doesn't have length

// Generic class
class GenericNumber<T> {
  zeroValue: T
  add: (x: T, y: T) => T

  constructor(zeroValue: T, add: (x: T, y: T) => T) {
    this.zeroValue = zeroValue
    this.add = add
  }
}

const myNumber = new GenericNumber<number>(0, (x, y) => x + y)
const myString = new GenericNumber<string>('', (x, y) => x + y)
```

### Decorators

```typescript
// Requires: "experimentalDecorators": true

// Class decorator
function sealed(constructor: Function) {
  Object.seal(constructor)
  Object.seal(constructor.prototype)
}

@sealed
class BugReport {
  type = 'report'
  title: string

  constructor(t: string) {
    this.title = t
  }
}

// Method decorator
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value

  descriptor.value = function(...args: any[]) {
    console.log(`Calling ${propertyKey} with`, args)
    const result = originalMethod.apply(this, args)
    console.log(`Result:`, result)
    return result
  }

  return descriptor
}

class Calculator {
  @log
  add(a: number, b: number) {
    return a + b
  }
}
```

### Migration Patterns

```javascript
// Step 1: Rename .js to .ts
// Step 2: Fix obvious errors
// Step 3: Add types gradually

// Before (JavaScript)
function getUser(id) {
  return fetch(`/api/users/${id}`).then(r => r.json())
}

// After (TypeScript)
interface User {
  id: number
  name: string
  email: string
}

async function getUser(id: number): Promise<User> {
  const response = await fetch(`/api/users/${id}`)
  return response.json()
}
```

---

## 🎓 Självutvärdering

### Efter Nivå 1-2
- [ ] Förstå varför typer är viktiga
- [ ] Basic types (string, number, boolean)
- [ ] Arrays och objects med typer

### Efter Nivå 3
- [ ] Interfaces och type aliases
- [ ] Generics
- [ ] Type guards

### Efter Nivå 4-5
- [ ] Utility types
- [ ] Mapped och conditional types
- [ ] Advanced patterns
- [ ] Migration strategies

---

## 📖 Ordlista

**Type**: Definition av vad något är
**Interface**: Kontrakt för objekts struktur
**Generic**: Typ som tar andra typer som parameter
**Union**: Typ A ELLER typ B
**Intersection**: Typ A OCH typ B
**Type Guard**: Kod som säkerställer typ
**Utility Type**: Inbyggd typ-transformation
**Discriminated Union**: Union med gemensam property

---

## 🆚 TypeScript vs JavaScript

| Feature | TypeScript | JavaScript |
|---------|-----------|-----------|
| **Typer** | Statisk | Dynamisk |
| **Kompilering** | Krävs | Nej |
| **Tooling** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Buggar** | Compile-time | Runtime |
| **Lärkurva** | Medel | Lätt |

---

## 🔗 Resurser

- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [TypeScript Playground](https://www.typescriptlang.org/play)
- [Total TypeScript](https://www.totaltypescript.com/)

---

## ❓ FAQ

**1. Måste jag använda TypeScript?**
Nej, men det rekommenderas för större projekt.

**2. Kan jag migrera gradvis?**
Ja! Byt ut .js till .ts fil för fil.

**3. Påverkar TypeScript performance?**
Nej, det kompileras till vanlig JavaScript.

**4. any vs unknown?**
unknown är säkrare - kräver type checking före användning.

**5. Interface vs Type?**
Interface för objekts struktur, Type för unions/intersections.

**6. Vad är tsconfig.json?**
Konfigurationsfil för TypeScript compiler.

**7. Hur debuggar jag TypeScript?**
Med source maps - browser debuggar original TS-kod.

**8. Fungerar TypeScript med React?**
Ja! React har excellent TypeScript support.

**9. Vad är .d.ts filer?**
Type declarations - typer för JavaScript libraries.

**10. Behöver jag typer för alla libraries?**
De flesta populära libraries har @types/library-name.

---

## 🎉 Grattis!

**Du kan nu:**
✅ Grundläggande TypeScript
✅ Interfaces och types
✅ Generics
✅ Advanced types
✅ Expert patterns

**Nästa steg:**
1. Konvertera ett JavaScript-projekt
2. Bygg ett TypeScript-projekt från scratch
3. Lär dig React med TypeScript
4. Utforska advanced patterns

**Lycka till! 🚀**

---

*Guide skapad 2024-11-17 | Version 1.0*
