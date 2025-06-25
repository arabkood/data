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
