#!/usr/bin/env bash
set -euo pipefail

service="${TWITTERAPI_IO_KEYCHAIN_SERVICE:-twitterapi.io}"
account="${TWITTERAPI_IO_KEYCHAIN_ACCOUNT:-${USER}}"

printf "TwitterAPI.io API key: " >&2
IFS= read -rs api_key
printf "\n" >&2

if [[ -z "${api_key}" ]]; then
  echo "empty key; abort" >&2
  exit 1
fi

security add-generic-password \
  -a "${account}" \
  -s "${service}" \
  -w "${api_key}" \
  -U

unset api_key
echo "stored twitterapi.io key in macOS Keychain service=${service} account=${account}" >&2
