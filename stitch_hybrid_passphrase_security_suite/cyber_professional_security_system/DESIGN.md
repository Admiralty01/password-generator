---
name: Cyber-Professional Security System
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#bbcabf'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#86948a'
  outline-variant: '#3c4a42'
  surface-tint: '#4edea3'
  primary: '#4edea3'
  on-primary: '#003824'
  primary-container: '#10b981'
  on-primary-container: '#00422b'
  inverse-primary: '#006c49'
  secondary: '#b7c8e1'
  on-secondary: '#213145'
  secondary-container: '#3a4a5f'
  on-secondary-container: '#a9bad3'
  tertiary: '#ffb3af'
  on-tertiary: '#650911'
  tertiary-container: '#fc7c78'
  on-tertiary-container: '#711419'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdad7'
  tertiary-fixed-dim: '#ffb3af'
  on-tertiary-fixed: '#410005'
  on-tertiary-fixed-variant: '#842225'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
  security-ultra: '#10B981'
  security-secure: '#F59E0B'
  security-weak: '#EF4444'
  surface-charcoal: '#1E293B'
  border-slate: '#334155'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  passphrase-display:
    fontFamily: JetBrains Mono
    fontSize: 22px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  metric-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-margin: 1.25rem
  stack-gap: 1rem
  element-padding: 1rem
  glass-padding: 1.5rem
---

## Brand & Style

The design system is engineered for high-stakes security environments, prioritizing trust, precision, and technical authority. The "Cyber-Professional" aesthetic blends the utilitarian clarity of developer tools with the refined polish of premium enterprise software. 

The visual narrative is built on the following pillars:
- **Authority through Precision:** Every element is aligned to a strict grid, utilizing thin, high-contrast borders and monospaced accents to evoke a sense of cryptographic accuracy.
- **Glassmorphic Depth:** Subtle translucency and backdrop blurs are used sparingly to create a sense of modern "layers of protection" without sacrificing legibility.
- **Data-Centric Visualization:** Security metrics (entropy, brute-force estimation) are treated as primary UI citizens, using clear geometric indicators and high-vibrancy status colors.
- **Technical Accessibility:** While the underlying logic is complex, the interface remains approachable through generous whitespace and a clear hierarchical structure.

## Colors

The palette is anchored in a deep "Midnight Slate" spectrum to reduce eye strain and provide a sophisticated backdrop for high-vibrancy status indicators.

- **Primary (Security Green):** Reserved for "Strong" and "Ultra" security states, as well as primary action triggers.
- **Surface Strategy:** The UI utilizes a layered approach. The base is the darkest slate, with "Surface Charcoal" used for elevated cards and containers to create depth.
- **Semantic Status:** 
  - **Security Ultra/Strong:** A vibrant emerald to signal safety.
  - **Security Secure:** A cautious amber for mid-tier entropy.
  - **Security Weak:** A muted, non-vibrant red to signal high risk without causing unnecessary alarm.
- **Accents:** Use slate grays for secondary text and borders to maintain a monochromatic, professional feel.

## Typography

This design system employs a dual-font strategy to balance human readability with technical precision.

- **UI Interface (Inter):** All navigation, headings, and body copy use Inter. Its neutral, high-legibility profile ensures that administrative tasks feel smooth and efficient.
- **Data & Passphrases (JetBrains Mono):** Critical security data—specifically generated passphrases, entropy bits, and character counts—must use JetBrains Mono. The monospaced nature prevents character confusion (e.g., 'i', 'l', '1') which is vital for security.
- **Styling:** Use `label-caps` for all-caps section headers to reinforce the "professional tool" aesthetic. Passphrases should always be rendered with increased letter spacing for maximum clarity during manual entry.

## Layout & Spacing

The layout follows a strict **Fixed-Fluid Hybrid** model optimized for mobile-first security interactions.

- **Grid:** A 4-column mobile grid with 20px margins. On larger mobile devices or tablets, the content container is capped at 480px to maintain focus.
- **Rhythm:** An 8px linear scaling system is used for all spacing. Elements are grouped in "functional blocks" using consistent 16px (1rem) gaps.
- **Passphrase Focus:** The generated output is centered vertically and horizontally, serving as the "Hero" of the interface. 
- **Reflow:** On desktop views, the interface remains centered with a max-width of 520px to mimic a handheld "security fob" or mobile authenticator experience.

## Elevation & Depth

Hierarchy in this design system is achieved through **Tonal Layering** and **Glassmorphism**, rather than traditional soft shadows.

- **Tiers of Trust:**
  - **Level 0 (Base):** Deep Slate (#0F172A).
  - **Level 1 (Cards):** Surface Charcoal (#1E293B) with a 1px Slate border (#334155).
  - **Level 2 (Active Modals/Overlays):** 20% opacity white fill with a 24px backdrop blur (Glassmorphism), wrapped in a high-contrast thin white border (10% opacity).
- **Shadows:** Only used for floating action buttons. Use a sharp, low-spread 4px shadow with 40% opacity of the background color to avoid "fuzziness" and maintain the "Cyber" aesthetic.

## Shapes

The shape language is "Soft-Technical." Elements use a subtle **4px (0.25rem)** corner radius for buttons and input fields. This ensures the UI feels modern and engineered, avoiding the extreme roundness associated with consumer social apps.

- **Standard Elements:** 4px radius (Soft).
- **Security Cards:** 8px radius (Large).
- **Status Pills:** 2px radius or sharp edges to emphasize a "data readout" feel.

## Components

- **Passphrase Display:** A high-contrast card using Level 2 elevation. It must include a "Copy" icon button and a "Refresh" icon button. Text is always centered and monospaced.
- **Security Gauge:** A horizontal segmented bar (12 segments). Color fills from left to right based on entropy. Segments transition from Red -> Amber -> Green.
- **Primary Action Buttons:** Solid Green (#10B981) with white monospaced text. High-contrast, no gradients.
- **Input Fields:** Darker than the surface background with a 1px border that glows (Primary Green) when focused. Labels should be in `label-caps`.
- **Status Chips:** Small, rectangular labels with monospaced text and a colored "dot" indicator to represent specific character types (symbols, numbers, uppercase).
- **Entropy Metrics:** Small-text data readouts placed directly below the passphrase, showing "Bits of Entropy" and "Time to Crack" in JetBrains Mono.