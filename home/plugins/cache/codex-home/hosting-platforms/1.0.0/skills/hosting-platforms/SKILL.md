---
name: hosting-platforms
description: Choose and coordinate deployment workflows across Vercel, Render, and Netlify. Use when the user wants to host or deploy a project but the provider is not fixed yet, or when comparing those platforms.
---

# Hosting Platforms

Use this skill to choose the right hosting target first, then hand off to the provider-specific workflow.

## Use this skill when

- The user wants to deploy or host a project but has not picked Vercel, Render, or Netlify yet.
- The user asks which of those platforms best fits a repository.
- The user wants to migrate between those hosting providers.

## Routing guide

- **Vercel**: best for frontend-heavy apps, preview deployments, Next.js projects, and teams already using Vercel workflows.
- **Render**: best for long-running services, worker processes, Blueprint-managed infrastructure, and apps that need databases or background jobs.
- **Netlify**: best for static or JAMstack sites, lighter publish flows, and teams centered on Netlify previews or site linking.

## Workflow

1. Inspect the repo's build system, runtime, and deployment shape.
2. Identify the required hosting primitives: static assets, SSR, long-running service, worker, preview URLs, database, cron, or edge functions.
3. Choose the best-fit hosting platform and explain the fit briefly.
4. Hand off to the provider-specific workflow:
   - `deploy-to-vercel` or `vercel-deploy`
   - `render-deploy`
   - `netlify-deploy`
5. Run the narrowest deployment or config validation needed for that target.

## Constraints

- Keep secrets out of logs and summaries.
- Prefer existing provider config when the repo already has one.
- Do not invent a cross-platform abstraction when a provider-specific workflow is already clear.
