import { printDataType } from "./print-typeof";

let consoleLogSpy;

beforeEach(() => {
  consoleLogSpy = jest.spyOn(console, "log").mockImplementation(() => {});
});

afterEach(() => {
  consoleLogSpy.mockRestore();
});

test('يجب أن تطبع "number" لقيمة رقمية', () => {
  // Arabic: "Should print 'number' for a numeric value"
  printDataType(100);
  expect(consoleLogSpy).toHaveBeenCalledWith("number");
});

test('يجب أن تطبع "string" لقيمة نصية', () => {
  // Arabic: "Should print 'string' for a string value"
  printDataType("hello");
  expect(consoleLogSpy).toHaveBeenCalledWith("string");
});

test('يجب أن تطبع "boolean" لقيمة منطقية', () => {
  // Arabic: "Should print 'boolean' for a boolean value"
  printDataType(true);
  expect(consoleLogSpy).toHaveBeenCalledWith("boolean");
  printDataType(false);
  expect(consoleLogSpy).toHaveBeenCalledWith("boolean");
});

test('يجب أن تطبع "undefined" لقيمة undefined', () => {
  // Arabic: "Should print 'undefined' for an undefined value"
  printDataType(undefined);
  expect(consoleLogSpy).toHaveBeenCalledWith("undefined");
  let x;
  printDataType(x);
  expect(consoleLogSpy).toHaveBeenCalledWith("undefined");
});

test('يجب أن تطبع "object" لقيمة كائن (بما في ذلك null والمصفوفة)', () => {
  // Arabic: "Should print 'object' for an object value (including null and array)"
  printDataType({});
  expect(consoleLogSpy).toHaveBeenCalledWith("object");
  printDataType([]);
  expect(consoleLogSpy).toHaveBeenCalledWith("object"); // typeof array is 'object'
  printDataType(null);
  expect(consoleLogSpy).toHaveBeenCalledWith("object"); // typeof null is 'object' (a known quirk)
});

test('يجب أن تطبع "function" لقيمة دالة', () => {
  // Arabic: "Should print 'function' for a function value"
  printDataType(() => {});
  expect(consoleLogSpy).toHaveBeenCalledWith("function");
  function myFunction() {}
  printDataType(myFunction);
  expect(consoleLogSpy).toHaveBeenCalledWith("function");
});
