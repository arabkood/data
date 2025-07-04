import { printTwoParameters } from "./print-two-params.js";

let consoleLogSpy;

afterEach(() => {
  if (consoleLogSpy) {
    consoleLogSpy.mockRestore();
  }
});

test("يجب أن تطبع معاملين نصيين ثابتين بشكل صحيح", () => {
  let output = "";

  consoleLogSpy = jest.spyOn(console, "log").mockImplementation((...args) => {
    output += args.join(" ") + "\n";
  });

  const p1 = "مرحباً";
  const p2 = "بالعالم";
  printTwoParameters(p1, p2);

  expect(output).toBe(`${p1}\n${p2}\n`);

  expect(consoleLogSpy).toHaveBeenCalledTimes(2);
  expect(consoleLogSpy).toHaveBeenNthCalledWith(1, p1);
  expect(consoleLogSpy).toHaveBeenNthCalledWith(2, p2);
});

const generateRandomString = (length = 10) => {
  let result = "";
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789أبتثجحخدذرزسشصضطظعغفقكلمنهوي !@#$%^&*()[]{};:,.<>?";
  const charactersLength = characters.length;
  for (let i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
};

test("يجب أن تطبع معاملات عشوائية بشكل صحيح لضمان عدم الغش", () => {
  // "Should print random parameters correctly to ensure no cheating"
  let output = "";
  consoleLogSpy = jest.spyOn(console, "log").mockImplementation((...args) => {
    output += args.join(" ") + "\n";
  });

  const randomParam1 = generateRandomString(Math.floor(Math.random() * 15) + 5);
  const randomParam2 = generateRandomString(Math.floor(Math.random() * 15) + 5);

  printTwoParameters(randomParam1, randomParam2);

  expect(output).toBe(`${String(randomParam1)}\n${String(randomParam2)}\n`);

  expect(consoleLogSpy).toHaveBeenCalledTimes(2);
  expect(consoleLogSpy).toHaveBeenNthCalledWith(1, randomParam1);
  expect(consoleLogSpy).toHaveBeenNthCalledWith(2, randomParam2);
});
