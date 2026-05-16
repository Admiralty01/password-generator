---
name: Secure Operations Interface
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#3c4a42'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#6c7a71'
  outline-variant: '#bbcabf'
  surface-tint: '#006c49'
  primary: '#006c49'
  on-primary: '#ffffff'
  primary-container: '#10b981'
  on-primary-container: '#00422b'
  inverse-primary: '#4edea3'
  secondary: '#565e74'
  on-secondary: '#ffffff'
  secondary-container: '#dae2fd'
  on-secondary-container: '#5c647a'
  tertiary: '#005ac2'
  on-tertiary: '#ffffff'
  tertiary-container: '#71a1ff'
  on-tertiary-container: '#00367a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#d8e2ff'
  tertiary-fixed-dim: '#adc6ff'
  on-tertiary-fixed: '#001a42'
  on-tertiary-fixed-variant: '#004395'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Hanken Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  mono-data:
    fontFamily: Geist
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 32px
  stack-sm: 4px
  stack-md: 12px
  stack-lg: 24px
---

## Brand & Style

This design system moves away from the "black-hat" terminal aesthetic toward a high-clarity, "white-hat" professional command center. The personality is defined by precision, vigilance, and transparency. It targets security analysts and IT administrators who require long-term readability and a sense of calm authority.

The style is a blend of **Corporate Modern** and **Technical Minimalism**. It utilizes a vast amount of whitespace to reduce cognitive load during high-alert situations. UI elements are rendered with architectural precision, favoring thin lines, subtle gradients, and a clear information hierarchy that emphasizes data over decoration.

## Colors

The palette is anchored by a clean, light-grey foundation (`#f8fafc`) to minimize glare and eye strain in office environments. 

- **Primary Security Green (#10b981):** Retained for its association with "Safe" and "Active" statuses, but applied with higher weight in text or as solid fills to ensure accessibility against light backgrounds.
- **Secondary Slate (#0f172a):** Used for primary typography and navigation backgrounds to provide a grounded, high-contrast anchor.
- **Accent Blue (#3b82f6):** Utilized for secondary actions, links, and informational states that do not require the urgency of green (safe) or red (alert).
- **Surface Neutrals:** A range of slates (from 50 to 200) define the scaffolding of the UI, creating subtle distinctions between sidebars, headers, and main content areas.

## Typography

The typography system prioritizes legibility and technical density. 

**Hanken Grotesk** is used for headlines to provide a sharp, contemporary feel that signals "modern technology." **Inter** handles the bulk of data entry and reading tasks due to its exceptional performance at small sizes. **Geist** is reserved for technical data, logs, and labels, providing a monospaced "developer-centric" touch to the security interface.

For mobile displays, `headline-xl` should scale down to 30px to prevent awkward line breaks in dense dashboards. All technical labels use uppercase tracking to distinguish them from standard body prose.

## Layout & Spacing

The layout follows a **structured fluid grid** model. On desktop, the interface utilizes a 12-column grid with generous 24px gutters to allow complex data visualizations to breathe.

- **Data Density:** Use a strict 8px base unit for all padding and margins. 
- **Containment:** Content is housed in "Surfaces" with consistent inner padding (usually 24px).
- **Responsive Behavior:** On mobile, the grid collapses to a single column with 16px side margins. Tablets utilize an 8-column grid.
- **Alignment:** All technical data points should be left-aligned with their corresponding headers to maintain a clear vertical scan line.

## Elevation & Depth

In this light theme, depth is communicated through **low-contrast outlines** and **ambient shadows** rather than glowing effects.

- **Level 0 (Base):** The background layer (`#f8fafc`).
- **Level 1 (Cards/Panels):** Pure white (`#ffffff`) background with a 1px border in Slate 200. A very soft shadow (0px 4px 12px rgba(0,0,0,0.03)) is applied to provide a subtle "lift."
- **Level 2 (Dropdowns/Popovers):** Pure white background with a slightly more pronounced shadow (0px 8px 24px rgba(0,0,0,0.08)) and a Slate 300 border.
- **Level 3 (Modals):** Centered with a dimmed backdrop (Slate 900 at 40% opacity) to focus the user's attention entirely on the critical task.

## Shapes

The shape language is "Soft" (`roundedness: 1`), utilizing a 4px (0.25rem) base radius. This small radius maintains the professional, technical discipline of the system while feeling more modern and approachable than sharp 0px corners.

- **Small elements (Buttons, Inputs, Badges):** 4px radius.
- **Large elements (Cards, Modals):** 8px radius (`rounded-lg`).
- **Indicators:** Circular (pill) shapes are reserved exclusively for status badges (e.g., "Online," "Threat Detected") to make them instantly recognizable as non-interactive status signals.

## Components

### Buttons
- **Primary:** Solid `#10b981` with white text. High-contrast and bold.
- **Secondary:** White background with `#0f172a` border and text.
- **Ghost:** No background, Slate 600 text; appears only on hover with a Slate 100 background.

### Input Fields
- **Default:** White background, 1px Slate 300 border.
- **Focus State:** 1px Primary Green border with a 3px soft green outer glow (20% opacity).
- **Labels:** Always persistent, positioned above the field in `label-caps` typography.

### Cards
- White background, 1px Slate 200 border.
- Header sections within cards should have a subtle bottom border to separate titles from data.

### Status Chips
- Small, pill-shaped components. Use light tinted backgrounds with dark text (e.g., Light Green background with Dark Green text) for high legibility without the heaviness of solid fills.

### Data Tables
- Row-based layout with subtle hover states (Slate 50).
- Use `mono-data` for IP addresses, timestamps, and hash values to ensure character alignment.