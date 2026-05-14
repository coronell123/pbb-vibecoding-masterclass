#!/usr/bin/env bash
# Pre-flight check for the Vibecoding workshop.
# Run once before you arrive: `bash check.sh`

set -u

ok()    { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail()  { printf "  \033[31m✗\033[0m %s\n" "$1"; FAILED=$((FAILED+1)); }
warn()  { printf "  \033[33m!\033[0m %s\n" "$1"; }
header(){ printf "\n\033[1m%s\033[0m\n" "$1"; }

FAILED=0

header "Checking your setup..."

# Node
if command -v node >/dev/null 2>&1; then
  NODE_VERSION=$(node -v | sed 's/v//')
  MAJOR=$(echo "$NODE_VERSION" | cut -d. -f1)
  if [ "$MAJOR" -ge 20 ]; then
    ok "Node.js $NODE_VERSION"
  else
    fail "Node.js $NODE_VERSION — need 20 or newer. Update at https://nodejs.org"
  fi
else
  fail "Node.js not found. Install from https://nodejs.org"
fi

# git
if command -v git >/dev/null 2>&1; then
  ok "git $(git --version | awk '{print $3}')"
else
  fail "git not found. Install from https://git-scm.com"
fi

# Claude Code
if command -v claude >/dev/null 2>&1; then
  ok "Claude Code installed ($(claude --version 2>/dev/null || echo 'version unknown'))"
else
  fail "Claude Code not installed. Run: npm install -g @anthropic-ai/claude-code"
fi

# Terminal sanity
if [ -n "${TERM:-}" ]; then
  ok "Terminal: $TERM"
else
  warn "TERM not set — may be fine, but try a different shell if Claude Code misbehaves"
fi

# Internet
if curl -s --max-time 5 https://api.anthropic.com >/dev/null 2>&1; then
  ok "api.anthropic.com reachable"
else
  warn "api.anthropic.com unreachable — check firewall/VPN before the workshop"
fi

header "Result"
if [ "$FAILED" -eq 0 ]; then
  printf "\n  \033[32mAll good. See you on the day.\033[0m\n\n"
  exit 0
else
  printf "\n  \033[31m%d issue(s) above.\033[0m Fix them, or message the instructor before the session.\n\n" "$FAILED"
  exit 1
fi
