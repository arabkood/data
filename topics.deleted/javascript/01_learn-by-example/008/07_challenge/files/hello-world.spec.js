let consoleLogSpy;

afterEach(() => {
  consoleLogSpy.mockRestore();
});

test('الناتج يجب أن يكون "hello world"', () => {
  let output = "";

  consoleLogSpy = jest.spyOn(console, "log").mockImplementation((...v) => {
    output += v.join(" ") + "\n";
  });

  require("./hello-world.js");

  expect(output).toEqual("hello world\n");
});
