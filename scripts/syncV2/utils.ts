export function h1(message: string) {
  const GREEN = "\x1b[1;32m";
  const RESET = "\x1b[0m";
  const width = 70;
  const banner = "=".repeat(width);

  console.log(`\n${GREEN}${banner}${RESET}`);
  console.log(`${GREEN}${message}${RESET}`);
  console.log(`${GREEN}${banner}${RESET}\n`);

  // Flush stdout immediately in Bun
  process.stdout.write("");
}

export function h2(message: string) {
  const BLUE = "\x1b[1;34m";
  const RESET = "\x1b[0m";
  const width = 50;
  const banner = "-".repeat(width);

  console.log(`${BLUE}${banner}${RESET}`);
  console.log(`${BLUE}${message}${RESET}`);
  console.log(`${BLUE}${banner}${RESET}`);

  // Flush stdout immediately in Bun
  process.stdout.write("");
}

function toCamel(str: string): string {
  return str.replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());
}

function toSnake(str: string): string {
  return str.replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);
}

export function camelCaseKeys(obj: any): any {
  if (obj instanceof Date) {
    return obj;
  }
  if (Array.isArray(obj)) {
    return obj.map(v => camelCaseKeys(v));
  } else if (obj !== null && typeof obj === 'object') {
    return Object.keys(obj).reduce((result, key) => {
      result[toCamel(key)] = camelCaseKeys(obj[key]);
      return result;
    }, {} as any);
  }
  return obj;
}

export function snakeCaseKeys(obj: any): any {
  if (obj instanceof Date) {
    return obj;
  }
  if (Array.isArray(obj)) {
    return obj.map(v => snakeCaseKeys(v));
  } else if (obj !== null && typeof obj === 'object') {
    return Object.keys(obj).reduce((result, key) => {
      result[toSnake(key)] = snakeCaseKeys(obj[key]);
      return result;
    }, {} as any);
  }
  return obj;
}
