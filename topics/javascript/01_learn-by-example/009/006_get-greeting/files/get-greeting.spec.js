import { getGreeting } from "./get-greeting";

test('يجب أن تعيد "أهلا" إذا كان المستخدم مسجلاً دخوله (isLoggedIn is true)', () => {
  const result = getGreeting(true);
  expect(result).toBe("أهلا");
});

test('يجب أن تعيد "الرجاء تسجيل الدخول!" إذا لم يكن المستخدم مسجلاً دخوله (isLoggedIn is false)', () => {
  const result = getGreeting(false);
  expect(result).toBe("الرجاء تسجيل الدخول!");
});
