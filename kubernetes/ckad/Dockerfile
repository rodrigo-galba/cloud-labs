FROM mcr.microsoft.com/playwright:v1.34.0-jammy
USER root
WORKDIR /tests
# # # Install Playwright dependencies
RUN npx @playwright/test install

RUN npx playwright install-deps

CMD ["npx", "playwright", "test"]