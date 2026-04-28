# -*- coding: utf-8 -*-
"""One-off emit of chunk_079_135.json and chunk_208_300.json. Run from repo root."""
import importlib.util
import json
from pathlib import Path


def item(
    id_num: int,
    question: str,
    difficulty: str,
    category: str,
    tags: list,
    answer: str,
    examples: list,
    tip: str,
    link_label: str,
    link_href: str,
) -> dict:
    return {
        "id": f"react-{id_num:03d}",
        "question": question,
        "difficulty": difficulty,
        "category": category,
        "tags": tags,
        "answer": answer,
        "examples": examples,
        "tip": tip,
        "links": [{"label": link_label, "href": link_href}],
    }


def ex(title: str, language: str, code: str, explanation: str) -> dict:
    return {"title": title, "language": language, "code": code, "explanation": explanation}


CH1 = [
    item(
        79,
        "What is React Router?",
        "beginner",
        "routing",
        ["react-router", "client-routing", "single-page-app"],
        """**React Router** is a **client-side routing** library for **React** apps. It **maps the URL in the address bar to UI trees**, so when users click links you change **what the page shows** without a full server **round trip** in a single-page app.

You typically wrap the app in a **router component** and declare **`<Route path=\"/path\" element={<Page />} />`** style config (v6) so navigation feels like a multi-page site while React keeps updating the same document.

Use it whenever you have **more than a single screen** and you want **shareable deep links and history** in a **React** bundle.""",
        [
            ex(
                "React Router v6: routes",
                "tsx",
                """import { createBrowserRouter, RouterProvider } from 'react-router-dom';\nimport { Home, About } from './pages';\n\nconst router = createBrowserRouter([\n  { path: '/', element: <Home /> },\n  { path: '/about', element: <About /> },\n]);\n\nexport function App() {\n  return <RouterProvider router={router} />;\n}\n""",
                "The browser `history` API updates, and the router supplies matching elements.",
            )
        ],
        "Say **declarative routes** and **code splitting** in larger apps, not a React core feature.",
        "React Router: home",
        "https://reactrouter.com/home",
    ),
    item(
        80,
        "How is React Router different from the history library?",
        "intermediate",
        "routing",
        ["react-router", "history", "stack"],
        """The **`history`** package is a **thin abstraction over the browser `History` and `location` API**. It can **push, replace, and listen** to URL changes, but it **does not render React** or know about components.

**React Router** **builds on that** (or the same concepts) to **connect URLs to a React element tree** with **Route matching, nested routes, and outlet composition**. In other words, **history** is **navigation state**; **React Router** is **UI routing for React** with conveniences like **data routers** in v6+.

In interviews, contrast **low-level history** vs **framework integration** and **outlets**.""",
        [
            ex(
                "Listener without React",
                "ts",
                """import { createBrowserHistory } from 'history';\n\nconst h = createBrowserHistory();\nconst u = h.listen(() => console.log(h.location.pathname));\n// h.push('/a');\n// later: u();\n""",
                "You get updates, not automatic component switching; React Router adds that layer.",
            )
        ],
        "Mention **createBrowserHistory**-style building blocks and that **v6+** leans on **data APIs**; history alone does not know about React.",
        "React Router: guides",
        "https://reactrouter.com/start/declarative/routing",
    ),
    item(
        81,
        "What are the components of React Router v6?",
        "intermediate",
        "routing",
        ["react-router", "v6", "data-router"],
        """In **v6+**, the common **surface area** is:

- **`createBrowserRouter` / `createHashRouter`**: build a **router object** (often with **data loaders and actions**).
- **`RouterProvider`**: mounts that router and is the app root in many new apps.
- **`<Route>` (in the route object tree)**: path patterns and **child routes**; **`element`** and **`index`**.
- **`<Link>` and `<NavLink>`**: declarative navigation without full page reloads.
- **`<Outlet>`**: renders the **active child** route in a layout route.
- **Hooks**: **`useParams`**, **`useSearchParams`**, **`useNavigate`**, **`useLocation`**, **`useRouteError`**, and data helpers like **`useLoaderData`**.

The exact mix depends on whether you use a **data router** or a lighter **`<BrowserRouter><Routes/></BrowserRouter>`** setup.""",
        [
            ex(
                "Data router (sketch)",
                "tsx",
                """import { createBrowserRouter, RouterProvider } from 'react-router-dom';\n\nconst r = createBrowserRouter([\n  { path: '/', element: <Layout />, children: [{ index: true, element: <Home /> }, { path: 'u/:id', element: <User /> }] },\n]);\n\nexport function App() {\n  return <RouterProvider router={r} />;\n}\n""",
                "`Layout` can render `<Outlet/>` and nested `Route` children map under `u/:id`.",
            )
        ],
        "Name **RouterProvider, Route tree, Link, Outlet, useNavigate, useParams** for a v6 screen score.",
        "React Router: route module",
        "https://reactrouter.com/routers/create-browser-router",
    ),
    item(
        82,
        "What is the purpose of the push and replace methods of history?",
        "intermediate",
        "routing",
        ["history", "navigation", "stack"],
        """In a browser or **`history` stack**, **`push` adds a new entry** to the back/forward list and moves there. The user can press **Back** to the previous page.

**`replace` swaps the current top entry** instead of appending, so the **previous item is not preserved** in the same way. You use **`replace` when a redirect is not worth an extra back step** (for example after a login, or to normalize a URL).

React Router v6+ exposes **`navigate(\'/path\', { replace: true })`** that mirrors the same idea with the `history` integration underneath.""",
        [
            ex(
                "navigate with replace (v6+)",
                "tsx",
                """import { useNavigate } from 'react-router-dom';\n\nexport function AfterLogin() {\n  const nav = useNavigate();\n  return <button onClick={() => nav('/home', { replace: true })}>Continue</button>;\n}\n""",
                "`replace: true` avoids stacking an intermediate /login in history.",
            )
        ],
        "Contrast **Back stack** vs **in-place** replacement; this is a classic browser interview detail.",
        "MDN: History",
        "https://developer.mozilla.org/en-US/docs/Web/API/History",
    ),
    item(
        83,
        "How do you programmatically navigate using React Router v4?",
        "intermediate",
        "routing",
        ["react-router", "v4", "imperative"],
        """In **React Router v4**, you get navigation props from **`<Route>`** render props or a **connected component**. The **`history` object** has **`push`, `replace`, and `go`**.

- **`this.props.history.push(\'/todos/12\')`** in class components, or
- In route components: **`<Route render={({ history }) => ...} />`**.

**v6** replaces that pattern with **`useNavigate`**, but the interview may still name **v4**—answer with **`history.push/replace`**. The core idea: **imperative navigation** still updates the URL and the matching route's UI.""",
        [
            ex(
                "v4 class push",
                "tsx",
                """import { withRouter, RouteComponentProps } from 'react-router-dom';\n\nclass NavBtn extends React.Component<RouteComponentProps> {\n  go = () => this.props.history.push('/done');\n  render() {\n    return <button onClick={this.go}>Done</button>;\n  }\n}\n\nexport const NavBtnRouted = withRouter(NavBtn);\n""",
                "`withRouter` injects `history` when you are not directly under a Route (older apps).",
            )
        ],
        "Bridge to v6: say **`useNavigate`** is the current hook; the mental model of **push/replace** is the same.",
        "React Router: v5 migration",
        "https://reactrouter.com/en/main/upgrading/v5#use-navigate-instead-of-historypush",
    ),
    item(
        84,
        "How do you get query parameters in React Router v4?",
        "intermediate",
        "routing",
        ["search-params", "location", "v4"],
        """In **v4/v5**, route components read **`this.props.location.search`**, a **string** like `?q=hi&sort=1`. You parse it with:

- **`URLSearchParams`**, or
- a helper such as **query-string** in older codebases.

With **`<Route children>` or `component`**, **`location` is** passed as part of **match/location history** props. You also can use **`this.props.location.pathname`** and combine.

In **v6+**, use **`useSearchParams`**, which is **more ergonomic** than hand-parsing, but the **parsing** idea is identical.""",
        [
            ex(
                "URLSearchParams",
                "ts",
        """import { RouteComponentProps } from 'react-router-dom';\n\nfunction getQuery(p: string) {\n  return new URLSearchParams(p).get('q');\n}\n\nexport function Search({ location }: RouteComponentProps) {\n  const q = getQuery(location.search);\n  return <p>Q: {q}</p>;\n}\n""",
                "You still re-parse on each location change, so v6's `useSearchParams` is nicer.",
            )
        ],
        "Mention **`useSearchParams`** for modern apps; keep **`URLSearchParams`** as the portable parser.",
        "MDN: URLSearchParams",
        "https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams",
    ),
    item(
        85,
        "Why do you get a \"Router may have only one child element\" warning?",
        "intermediate",
        "routing",
        ["react-router", "v4", "children"],
        """Older **React Router (v2/v3 style)** and some **v4** patterns wrapped content with **`<Router>`** where the router **expected exactly one child element** in certain APIs so it could **clone and inject** props. If you pass **sibling elements** (two top-level children), React sees **an array/fragment of multiple roots** and the router's **assumption is broken**, so a warning appears.

**Fix:** **wrap in a parent** (`<div>`, or **`<></>` in React 16+**), or in modern **v6+** you generally **use `RouterProvider` or a single `Routes` tree** where this is less of a footgun.

In legacy code, this often meant **one composed layout component** as the only child of `Router`/`BrowserRouter`""",
        [
            ex(
                "Single wrapper",
                "tsx",
                """import { BrowserRouter, Route } from 'react-router-dom';\n\nexport function App() {\n  return (\n    <BrowserRouter>\n      <div>\n        <Route path=\"/\" element={<Home />} />\n        <Route path=\"/a\" element={<A />} />\n      </div>\n    </BrowserRouter>\n  );\n}\n""",
                "A single `div` satisfies one-child rules in the older design.",
            )
        ],
        "Relate the warning to **the older injection pattern**; today prefer **a single `Routes` root** in v6.",
        "React Router: FAQ (legacy context)",
        "https://github.com/remix-run/react-router/blob/main/FAQ.md",
    ),
    item(
        86,
        "How do you pass params to the history.push method in React Router v4?",
        "intermediate",
        "routing",
        ["history", "params", "v4"],
        """**`history.push` takes a string path** or a **location object** in many setups. The usual pattern is to **string-interpolate** dynamic segments into the path, for example **`history.push(`/users/${id}`)**, and let **the Route path `'/users/:id'`** read **`useParams` / `match.params`** in the child (v4 used **`match.params`** on the matched route component).

**Query** pieces go in **`?search=...`**, and **state** can ride on **`location.state`** with **`push({ pathname, search, state })`** form when supported by your history version.

**v6+:** **`navigate(`/users/${id}`)** or an object to **`useNavigate`**.""",
        [
            ex(
                "String path with id",
                "tsx",
        """// v4: history.push(`/todos/${id}`);\n// v6+:\nimport { useNavigate } from 'react-router-dom';\n\nexport function Row({ id }: { id: string }) {\n  const n = useNavigate();\n  return <button onClick={() => n(`/todos/${id}`)}>Open</button>;\n}\n""",
                "The important idea is: **param values land in the URL string** and are parsed by the router.",
            )
        ],
        "Do not confuse **URL params** (`:id`) with **query params**; both can coexist.",
        "React Router: useParams",
        "https://reactrouter.com/hooks/use-params",
    ),
    item(
        87,
        "How do you implement a default or NotFound page?",
        "intermediate",
        "routing",
        ["404", "catch-all", "react-router"],
        """You register a **catch-all** route. In **v6**, use a **path of `'*'`** (or a dedicated **404 route**) as a **sibling** so it matches any unmatched path; keep it **last** in the `children` order when using nested data routers, or in flat `Routes` use **`<Route path=\"*\" element={<NotFound/>}/>`**.

A **default child** in a layout uses **`index` routes**; a **not-found** is different: it is the **unmatched** pattern.

**Server-side:** your host should still **serve the SPA** on unknown paths, or 404s return HTML for the client router to then show the 404 view.""",
        [
            ex(
                "Catch-all in v6",
                "tsx",
        """import { Route, Routes } from 'react-router-dom';\nimport { Home, NotFound } from './pages';\n\nexport function AppRoutes() {\n  return (\n    <Routes>\n      <Route path=\"/\" element={<Home />} />\n      <Route path=\"*\" element={<NotFound />} />\n    </Routes>\n  );\n}\n""",
                "Order matters: static routes first, `*` after.",
            )
        ],
        "Mention **server config** (always `index.html` for SPA) separate from the **client `*` route**.",
        "React Router: not found",
        "https://reactrouter.com/en/main/start/tutorial#handling-not-found-errors",
    ),
    item(
        88,
        "How do you get history in React Router v4?",
        "intermediate",
        "routing",
        ["history", "withrouter", "v4"],
        """In **v4/v5** you obtain **`history` by**:

- Receiving it as a prop from **`<Route component={...}>`** or **`render` props**, or
- Using **`withRouter` higher-order component** to inject **`history`, `location`, and `match`** when your component is not a direct `Route` child, or
- In connected Redux apps, sometimes via **`connected-react-router`**.

**v6** removes `history` from props: use **`useNavigate`**, **`useLocation`**, and **router APIs** on `RouterProvider` data routers. Answer v4 concretely; mention the hook migration to show awareness.""",
        [
            ex(
                "withRouter (v4/v5 idea)",
                "tsx",
        """// import { withRouter } from 'react-router-dom';\n// export default withRouter(MyComponent);\n// MyComponent receives history, location, match\n\nimport { useNavigate, useLocation } from 'react-router-dom';\n\nexport function MyComponent() {\n  const n = useNavigate();\n  const l = useLocation();\n  return <button onClick={() => n(-1)}>Back from {l.pathname}</button>;\n}\n""",
                "The modern v6 way replaces the injected `history` object.",
            )
        ],
        "Say `withRouter` and **Route props** for legacy; `useNavigate` for new code.",
        "React: Blog on React Router 6",
        "https://reactrouter.com",
    ),
    item(
        89,
        "How do you perform an automatic redirect after login?",
        "intermediate",
        "routing",
        ["auth", "redirect", "navigate"],
        """After a successful **login** you **navigate the user to a safe route** and often **`replace: true`** so the login screen is not an extra back step.

- **v6:** **`navigate(from, { replace: true })`**, or return **`<Navigate to=... replace />`** in JSX when a route should guard and bounce.
- **v4/v5:** **`history.replace('/app')`**.

Also preserve a **`from` location** in **`location.state` or `?redirect=`** to send users back to the page they tried to open, which is a better UX for protected routes.""",
        [
            ex(
                "post-login replace",
                "tsx",
        """import { useNavigate, useLocation } from 'react-router-dom';\nimport { useState } from 'react';\n\nexport function Login() {\n  const nav = useNavigate();\n  const loc = useLocation() as { state?: { from?: { pathname: string } } };\n  const [err, setErr] = useState('');\n  async function submit() {\n    await fakeLogin();\n    const to = loc.state?.from?.pathname ?? '/home';\n    nav(to, { replace: true });\n  }\n  return <button onClick={submit}>Sign in</button>;\n}\n\nasync function fakeLogin() { /* */ }\n""",
                "Carrying `from` in state is a common `ProtectedRoute` pattern.",
            )
        ],
        "Pair with **httpOnly session cookies** or **tokens**; redirect is just UI navigation.",
        "React Router: Navigate",
        "https://reactrouter.com/components/navigate",
    ),
    item(
        90,
        "What is React Intl?",
        "beginner",
        "i18n",
        ["react-intl", "formatjs", "localization"],
        """**FormatJS React Intl** (often called **react-intl**) is a set of **React components and hooks** for **internationalization** built on the **ICU** message model. It helps you **translate strings**, **pluralize**, **format numbers and dates per locale**, and keep **message catalogs** in JSON.

It is a **mature, widely used** solution when you do not get i18n from a framework. You provide **`IntlProvider` with `locale` and `messages`**, and render **`FormattedMessage`** or **`useIntl`** in components.""",
        [
            ex(
                "Provider shell",
                "tsx",
        """import { IntlProvider } from 'react-intl';\nimport en from './en.json';\n\nconst messages: Record<string, string> = en;\n\nexport function App() {\n  return (\n    <IntlProvider locale=\"en\" messages={messages}>\n      <Main />\n    </IntlProvider>\n  );\n}\n""",
                "The catalog maps message ids to translated strings for the current locale.",
            )
        ],
        "Mention **ICU** and that **formatjs** is the umbrella project name today.",
        "Format.js: getting started",
        "https://formatjs.io/docs/getting-started/installation",
    ),
    item(
        91,
        "What are the main features of React Intl?",
        "intermediate",
        "i18n",
        ["react-intl", "formatjs", "icu"],
        """Core features include **message translation with id keys**, **rich text and placeholders in messages**, **plural, select, and number formatting using ICU rules**, and **date/time/relative time formatting** with **`@formatjs/intl` polyfills** when a runtime lacks a feature.

**React bindings** add **`FormattedMessage`**, **`FormattedDate`**, and **`useIntl()`** to access `formatMessage` imperatively, plus **Extraction/compilation** tooling in larger apps.

Teams pair it with **locale-aware routing** and **lazy-loaded message bundles** per language.""",
        [
            ex(
                "Plurals (conceptual)",
                "json",
        """{\n  \"itemCount\": \"{count, plural, =0 {No items} one {# item} other {# items}}\"\n}\n""",
                "ICU plural rules are a headline feature over naive string replace.",
            )
        ],
        "Name **ICU message syntax**, `IntlProvider`, and `useIntl` as the day-one trio.",
        "Format.js: React Intl",
        "https://formatjs.io/docs/react-intl",
    ),
    item(
        92,
        "What are the two ways of formatting in React Intl?",
        "intermediate",
        "i18n",
        ["react-intl", "formatmessage", "components"],
        """1) **Declarative** with **components** like **`FormattedMessage`**, **`FormattedDate`**, **`FormattedNumber`**, and **`FormattedRelativeTime`**, which read **`intl` from context** and render the formatted output.

2) **Imperative** with **`const intl = useIntl()`** and then **`intl.formatMessage`**, **`intl.formatDate`**, and similar, which is good when a **string** must be passed to a child prop or a **non-JSX API**.

Both ultimately use the **same underlying formatter**; choose based on where you need the value.""",
        [
            ex(
                "Imperative vs component",
                "tsx",
        """import { FormattedMessage, useIntl } from 'react-intl';\n\nexport function A() {\n  const intl = useIntl();\n  const title = intl.formatMessage({ id: 'app.title' });\n  return (\n    <section aria-label={title}>\n      <h1>\n        <FormattedMessage id=\"app.title\" defaultMessage=\"Hello\" />\n      </h1>\n    </section>\n  );\n}\n""",
                "Use `formatMessage` when a plain string is required for attributes.",
            )
        ],
        "Call out **a11y attributes** often need imperative `formatMessage`.",
        "useIntl: formatMessage",
        "https://formatjs.io/docs/react-intl#useintl",
    ),
    item(
        93,
        "How do you use FormattedMessage as a placeholder with React Intl?",
        "intermediate",
        "i18n",
        ["formattedmessage", "placeholders", "values"],
        """Use **`values`** on **`FormattedMessage`** to **inject dynamic segments** and optional **rich** elements. The message string in the catalog uses **ICU placeholders** like `{name}` or richer tags, and the **`values` prop** supplies them.

For **rich** translations you can also pass **React element values** in **`values`**, and mark parts of a sentence with custom tags the translator controls.

If you need the **string only**, prefer **`useIntl().formatMessage`** to avoid an extra wrapper element.""",
        [
            ex(
                "values prop",
                "tsx",
        """import { FormattedMessage } from 'react-intl';\n\nexport function Hi({ who }: { who: string }) {\n  return (\n    <p>\n      <FormattedMessage id=\"greet.user\" defaultMessage=\"Hello, {name}!\" values={{ name: who }} />\n    </p>\n  );\n}\n""",
                "`{name}` is filled from `values.name`.",
            )
        ],
        "Be careful to **not embed user HTML**; treat rich text as structured elements, not raw HTML strings, unless you sanitize.",
        "FormattedMessage",
        "https://formatjs.io/docs/react-intl/components#formattedmessage",
    ),
    item(
        94,
        "How do you access the current locale with React Intl?",
        "beginner",
        "i18n",
        ["locale", "useIntl", "context"],
        """Read **`useIntl().locale`**, or **pull `locale` from `context`** if you are inside **`IntlProvider`**. The provider is the **source of truth**; hooks should be used **inside** that tree.

You can also **lift locale state** in your app (for example a user setting) and pass **`locale=...` down** to the provider, switching catalogs when the user changes language.

For **SSR** you pick **locale** from the **Accept-Language** header, route segment, or cookie, then set **`IntlProvider`** on the client.""",
        [
            ex(
                "useIntl().locale",
                "tsx",
        """import { useIntl } from 'react-intl';\n\nexport function LanguageChip() {\n  const { locale } = useIntl();\n  return <span className=\"badge\">{locale}</span>;\n}\n""",
                "The same hook exposes `formatMessage` and the active locale string.",
            )
        ],
        "Mention you **re-render** the subtree when you change the provider's `locale` and `messages` together.",
        "React Intl: API",
        "https://formatjs.io/docs/react-intl#locale",
    ),
    item(
        95,
        "How do you format a date using React Intl?",
        "beginner",
        "i18n",
        ["dates", "formatjs", "intl"],
        """Use **`FormattedDate`**, **`FormattedTime`**, or **`useIntl().formatDate` / `formatTime`** with the **`value`** prop/argument. You can pass **`dateStyle`/`timeStyle`**-like options in modern `Intl` options objects supported by the polyfill you ship.

`formatDateToParts` (via the underlying intl) can help you **interleave** literal text in complex layouts, but the common path is a single **`formatDate(new Date(), { year: 'numeric', month: 'long', day: 'numeric' })` style options object**.""",
        [
            ex(
                "formatDate with useIntl",
                "tsx",
        """import { useIntl, FormattedDate } from 'react-intl';\n\nexport function Post({ d }: { d: string }) {\n  const { formatDate } = useIntl();\n  const t = new Date(d);\n  return (\n    <p title={formatDate(t, { dateStyle: 'full' })}>\n      Posted <FormattedDate value={t} year=\"numeric\" month=\"long\" day=\"2-digit\" />\n    </p>\n  );\n}\n""",
                "Component vs function mirrors the two formatting styles question.",
            )
        ],
        "Remember **time zones** and that **`Date`** parsing from strings is easy to get wrong; often store **ISO UTC** and render in a chosen zone for apps that need it.",
        "MDN: Intl.DateTimeFormat",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat",
    ),
    item(
        96,
        "What is the Shallow Renderer in React testing?",
        "intermediate",
        "testing",
        ["shallow", "test-renderer", "enzyme"],
        """The **shallow renderer** (historically in **`react-test-renderer/shallow`**) **renders a component one level deep**, stubbing child components so you assert **the props and tag your component would issue** without mounting the full tree.

**Enzyme**'s `shallow()` popularized the pattern. This was useful in older **class and HOC** heavy code to **avoid deep side effects** in child subtrees. With **function components, hooks, and testing-library's user-centric** guidance, many teams **shallow test less** today, favoring **integration-style tests** for behavior.

**React 18+** testing guidance often prefers **`@testing-library/react`**, not shallow-only snapshots of implementation details.""",
        [
            ex(
                "react-test-renderer/shallow (conceptual)",
                "tsx",
        """// Legacy pattern (avoid in new work unless maintaining old tests):\n// import ShallowRenderer from 'react-test-renderer/shallow';\n// const r = new ShallowRenderer();\n// r.render(<MyForm />);\n// const out = r.getRenderOutput();\n\n// Prefer @testing-library/react to query the real DOM in jsdom\nimport { render, screen } from '@testing-library/react';\n\ntest('label', () => {\n  render(<button>ok</button>);\n  expect(screen.getByRole('button', { name: 'ok' })).toBeInTheDocument();\n});\n""",
                "Contrast shallow vs RTL which encourages DOM queries and behavior.",
            )
        ],
        "If asked in legacy interviews, explain the **isolation** benefit; in modern ones, state **you prefer RTL** and avoid over-mocking children.",
        "Testing Library: guiding principles",
        "https://testing-library.com/docs/guiding-principles",
    ),
    item(
        97,
        "What is the TestRenderer package in React?",
        "intermediate",
        "testing",
        ["react-test-renderer", "snapshot", "fiber"],
        """**`react-test-renderer`** is an **official** package that **renders React elements to a pure JavaScript object tree** instead of a real DOM, useful in **Jest** for **snapshots and introspection** without a browser. It is **not a replacement** for `react-dom/client` in production.

It is helpful for **low-level** checks and **synchronous** traversal of the output, but for app tests many teams use **`@testing-library/react`**, which uses **jsdom** and focuses on **user-visible** outcomes.

`createRoot` from **react-test-renderer** API evolved alongside React; check the current docs for the exact entry point used in your version.""",
        [
            ex(
                "tree JSON snapshot idea",
                "tsx",
        """import TestRenderer from 'react-test-renderer';\nimport { Greet } from './Greet';\n\ntest('snapshot (discouraged for behavior)', () => {\n  const t = TestRenderer.create(<Greet name=\"A\" />);\n  expect(t.toJSON()).toMatchSnapshot();\n});\n""",
                "Snapshots of JSON trees are brittle; prefer queries for behavior in new tests.",
            )
        ],
        "Connect to **@testing-library** as the more typical choice for **product** tests in 2024+ codebases.",
        "react-test-renderer (npm)",
        "https://www.npmjs.com/package/react-test-renderer",
    ),
    item(
        98,
        "What is the purpose of the ReactTestUtils package?",
        "intermediate",
        "testing",
        ["react-dom-test-utils", "legacy", "events"],
        """**`react-dom/test-utils` (classically ReactTestUtils)** had helpers to **find DOM nodes, simulate events, and act()** around state updates in **older test stacks** before the **`act` API** was centralized. Many helpers were for **class components and legacy** patterns.

Today **`@testing-library/user-event`**, **RTL**'s `fireEvent`, and **React 18**'s unified **`act` from 'react'** (or the testing package you import from) are the **default tools**. The older utils still exist in places but are not where new tests should start.

`act` is still essential to **flush effects** in tests, now commonly **wrapped** by **RTL** automatically in many cases.""",
        [
            ex(
                "act pattern",
                "tsx",
        """import { act } from 'react';\nimport { useState } from 'react';\nimport { createRoot } from 'react-dom/client';\nimport { screen } from '@testing-library/react';\n\n// RTL wraps many updates; for manual act you might still do:\n// await act(async () => { /* trigger */ });\n""",
                "You rarely import TestUtils for new work; you import RTL and user-event instead.",
            )
        ],
        "Emphasize **act** and **RTL** as the current story, not a huge ReactTestUtils surface in new code.",
        "React: act",
        "https://react.dev/reference/react/act",
    ),
    item(
        99,
        "What is Jest?",
        "beginner",
        "testing",
        ["jest", "runner", "snapshots"],
        """**Jest** is a **JavaScript test runner** by Meta, widely used in **React** and **Node** projects. It **discovers tests**, **mocks modules**, and **reports** results with a great **watch mode** and **snapshot** support.

Jest **ships with jsdom** integration patterns (often via your test environment config) to run **component tests** in Node, and with **Babel/TS transforms** it executes **TypeScript** tests.

**Vitest** is a popular Jest alternative in Vite codebases, but the **Jest** mental model of **describe/it/expect** and **mocks** is the standard interview language.""",
        [
            ex(
                "Sample test",
                "ts",
        """import { add } from './math';\n\ntest('adds', () => {\n  expect(add(1, 2)).toBe(3);\n});\n""",
                "This is the basic shape even before React is involved.",
            )
        ],
        "Mention **ts-jest** or **Babel** only if asked how TS runs; the default in CRA/Vite may differ (Vitest).",
        "Jest: Getting started",
        "https://jestjs.io/docs/getting-started",
    ),
    item(
        100,
        "What are the advantages of Jest over Jasmine?",
        "intermediate",
        "testing",
        ["jest", "jasmine", "mocking"],
        """**Jest** ships **batteries included**: a **test runner, assertion library, snapshot testing, and powerful module mocking** with a focus on a **single** coherent CLI and **zero-config** defaults in many stacks.

**Jasmine** is a **BDD** framework; historically you **wired Karma** in browsers, **assertion styles** differ, and the **ecosystem** in modern **React+Node** skews to **Jest** or **Vitest**.

Jest's **isolation and hoisted mocks** are familiar to most teams, and the **JSDOM** story for **React** is well trodden. Jasmine still appears in some Angular or legacy setups.""",
        [
            ex(
                "Jest auto mock sketch",
                "ts",
        """ jest.mock('./api', () => ({ fetchUser: () => Promise.resolve({ id: '1' }) })); """,
                "Jest's mocking is a differentiator vs older Jasmine+Require stacks.",
            )
        ],
        "Be neutral: if the team is **Jasmine+Karma** legacy, note **migration to Jest/Vitest** is common, not a religious war.",
        "Jest: Mock functions",
        "https://jestjs.io/docs/mock-functions",
    ),
    item(
        101,
        "Can you give a simple example of a Jest test case?",
        "beginner",
        "testing",
        ["jest", "example", "unit-test"],
        """A Jest file uses **`test` (or `it`)** and **`expect`**. The runner executes each test function and prints **pass/fail**. For React, you **render** a component in **jsdom** and **assert the DOM** with **Testing Library** (preferred) or a basic snapshot with **react-test-renderer**.

Keep tests **one behavior per `it`**, use **accessibility role queries** when possible, and **avoid** testing implementation details like internal state or private function names when you can assert the **output on screen** instead.""",
        [
            ex(
                "Jest + RTL",
                "tsx",
                """import { render, screen } from '@testing-library/react';\nimport userEvent from '@testing-library/user-event';\nimport { Counter } from './Counter';\n\ntest('increments on click', async () => {\n  const u = userEvent.setup();\n  render(<Counter />);\n  await u.click(screen.getByRole('button', { name: /more/i }));\n  expect(screen.getByText('1')).toBeInTheDocument();\n});\n""",
                "User-event simulates a real user path; the assertion reads visible text or roles.",
            )
        ],
        "Show you know **user-event** over raw `click` in serious apps; it is the modern default in RTL examples.",
        "Jest: Expect",
        "https://jestjs.io/docs/expect",
    ),
    item(
        102,
        "What is Flux?",
        "intermediate",
        "state-management",
        ["flux", "unidirectional", "facebook"],
        """**Flux** is an **architectural pattern** (popularized with React) for **unidirectional data flow** to avoid the tangled two-way **MV** patterns. It centers on a **Dispatcher**, **actions**, and **stores** that emit change events so **views re-render in a clear direction**.

**Redux** is a **simplified** implementation of the **Flux** ideas, but the interview word **Flux** is the **conceptual** umbrella (dispatcher + stores) rather than a specific npm name today. Many new apps use **context**, **Zustand**, or **Server Components** for parts of the problem instead of a classic Flux app.""",
        [
            ex(
                "Action shape (toy idea)",
                "ts",
        """type Action = { type: 'ADD_TODO'; text: string };\n// Stores listen and update; views subscribe.\n""",
                "In Flux the dispatcher fans actions out; stores keep domain state.",
            )
        ],
        "Contrast with **MVC** tangling; in Flux **data flows in one main loop**.",
        "Redux: History (Flux family)",
        "https://redux.js.org/understanding/history-and-design/flux",
    ),
    item(
        103,
        "What is Redux?",
        "beginner",
        "state-management",
        ["redux", "store", "reducer"],
        """**Redux** is a small **state container** with **one global store** that updates through **pure `reducer` functions** in response to **plain action objects**. The store is **predictable, serializable, and testable** and pairs with **react-redux** to wire React components to slices of state and dispatchers.

New codebases usually adopt **Redux Toolkit** (`@reduxjs/toolkit`) to reduce boilerplate, keep reducers in **`createSlice`**, and use **`configureStore`**. The interview answer should still name **the three principles: single state tree, actions as plain objects, and pure reducers**.""",
        [
            ex(
                "createSlice sketch",
                "ts",
        """import { createSlice, configureStore } from '@reduxjs/toolkit';\n\nconst counter = createSlice({\n  name: 'counter',\n  initialState: 0,\n  reducers: { inc: s => s + 1 },\n});\n\nexport const store = configureStore({ reducer: { c: counter.reducer } });\n""",
                "RTK is the on-ramp; classic `createStore` is legacy teaching material today.",
            )
        ],
        "Say you reach for **RTK** first; the mental model in interviews is the same as classic Redux.",
        "Redux: Getting started",
        "https://redux.js.org/introduction/getting-started",
    ),
    item(
        104,
        "What are the core principles of Redux?",
        "intermediate",
        "state-management",
        ["redux", "principles", "single-source"],
        """1) **Single source of truth:** one **object tree** in a single `store` makes debugging and devtools replay possible.

2) **State is read-only** except through **emitted action objects** that describe *what* happened, not *how* to change references by surprise.

3) **Reducers are pure functions** of `(state, action) => newState` with **no side effects** in the reducer body.

Middleware handles **I/O, logging, and async** so reducers stay **serializable, replayable, and testable**.""",
        [
            ex(
                "Why pure reducer",
                "ts",
        """// Bad: side effect inside reducer (do not do this)\n// function r(state, a) { fetch('/x'); return state; }\n\n// Good: return new object/array immutably\n""",
                "Side effects belong in middleware, listeners, thunks, or query layers.",
            )
        ],
        "Name **devtool time travel** and **replay of actions** as why purity matters in practice.",
        "Redux: Three principles",
        "https://redux.js.org/understanding/three-principles",
    ),
    item(
        105,
        "What are the downsides of Redux compared to Flux?",
        "intermediate",
        "state-management",
        ["redux", "flux", "tradeoffs"],
        """**Redux** keeps **one** store, which is simple for tooling but can become a **large tree** to partition carefully. **Classic Flux** allowed **multiple stores** in some apps, which could isolate domains but was **harder to reason about** across teams.

**Redux** also encourages **a lot of ceremony** in older hand-written patterns, though **RTK** and **slices** fix much of that. Both patterns can be **overkill** for small UIs that only need `useState`+`useContext` or a tiny global store (Zustand, Jotai, etc.).

**Net:** Redux is **simpler in rules** (one source of truth) but **bigger in scale**; Flux as a *family* is more flexible, yet **inconsistent** across codebases if many stores differ.""",
        [
            ex(
                "When not to add Redux",
                "text",
        """Local form drafts and one-off modals are often `useState` in the nearest parent until shared needs appear.""",
                "Shows you avoid global store bloat in interviews.",
            )
        ],
        "Be honest: **not every** React screen needs a global app store.",
        "Redux: When should I use Redux",
        "https://redux.js.org/faq/general#when-should-i-use-redux",
    ),
    item(
        106,
        "What is the difference between mapStateToProps() and mapDispatchToProps()?",
        "intermediate",
        "state-management",
        ["react-redux", "connect", "props"],
        """In **`connect()` from react-redux (classic API)**, **`mapStateToProps` selects slices** of the Redux store to **inject as component props** so React re-renders when those slices change, while **`mapDispatchToProps` wires action creators (or `dispatch` calls)** to **callback props** so the UI can dispatch without importing `useDispatch` (hooks were not available when this pattern was primary).

- **`mapStateToProps`**: `state => { visible todos }` and optionally `(state, ownProps)`.
- **`mapDispatchToProps`**: object shorthand `{ increment }` or function form `(dispatch, ownProps) => bound`.

**Modern code** prefers **`useSelector` and `useDispatch` hooks**; `connect` remains in many legacy class components.""",
        [
            ex(
                "Object shorthand of mapDispatch (idea)",
                "ts",
        """import { addTodo } from './actions';\n// const mapD = { addTodo };\n// same as { addTodo: (...a) => dispatch(addTodo(...a)) } with bindActionCreators\n""",
                "The object form calls `bindActionCreators` under the hood in connect.",
            )
        ],
        "Always mention **`ownProps`** in both mappers and how you avoid heavy selectors without **reselect**.",
        "useSelector: React Redux",
        "https://react-redux.js.org/api/hooks#useselector",
    ),
    item(
        107,
        "Can you dispatch an action in a reducer?",
        "intermediate",
        "state-management",
        ["redux", "reducer", "purity"],
        """**You should not.** The **reducer** must be **synchronous, pure, and free of side effects** like `dispatch` calls, network, timers, or randomness. A reducer only **returns the next state** for the given `action` type.

Firing a **cascade of actions** from inside a reducer would **break** **DevTools** replay, **time travel**, and **testing**, and can cause **infinite** update loops. Instead, use **listener middleware, thunks, sagas, RTK Query, or a separate effect layer** to coordinate multiple updates.

If you need a **chained** update, the usual pattern is **one reducer** handling a single action, or a **thunk** dispatching a sequence, not reducers calling each other through `dispatch` directly.""",
        [
            ex(
                "What to do instead",
                "ts",
        """// inside createAsyncThunk (RTK) you may dispatch other actions; not inside a slice reducer's case function.\n""",
                "Side-effectful orchestration belongs outside pure reducers.",
            )
        ],
        "A crisp interview line: **reducers are pure; dispatch is a side effect** even if the API looks tempting.",
        "Redux: Reducers are pure",
        "https://redux.js.org/understanding/thinking-in-redux/three-principles#reducers-are-pure-functions",
    ),
    item(
        108,
        "How do you access the Redux store outside a component?",
        "intermediate",
        "state-management",
        ["redux", "getstate", "modules"],
        """Import the **singleton store** (from where you `configureStore`) and call **`store.getState()`** or **`store.dispatch`**. In RTK, export **`store` from your store file** and use it in **rare** places like **API client interceptors** (token refresh) or **some** legacy code.

Another pattern: **`getStore` accessor** in a small module, set once at app bootstrap, so tests can inject a test store. Avoid abusing this for general UI updates—**components** should go through **hooks** or `connect` so they **re-render** when the store changes.

**Server-side** rendering and **Next.js** may build **a store per request**; never use a true global in those environments unless it is per-request instance.""",
        [
            ex(
                "getState in interceptor",
                "ts",
        """import { store } from './store';\n\n// axios.interceptors.response.use((r) => r, (err) => { const t = store.getState().auth.token; /* refresh */ });\n""",
                "Only use direct access where React lifecycle is not available.",
            )
        ],
        "Emphasize **per-request** store in apps that do SSR, not a leaked singleton across users.",
        "Redux: Store API",
        "https://redux.js.org/api/store#getstate",
    ),
    item(
        109,
        "What are the drawbacks of the MVW pattern?",
        "intermediate",
        "architecture",
        ["mvw", "angularjs", "two-way"],
        """**Model-View-Whatever** (e.g. **AngularJS**'s `ng-model` style) leans on **two-way** bindings that can make it **unclear** where a change was initiated when **views** can write **models** and models push **back** in several directions.

That often leads to **harder debugging, circular updates, and spurious watchers** at scale, compared with a **unidirectional** flow. Modern front-end leans to **unidirectional** patterns (Redux, Flux) or **explicit data libraries** and **reactive** pipelines with **clear** ownership.

**Drawbacks in interviews:** **implicit coupling, harder reasoning about large screens, and more surprise updates**; pair with a note that some MVW is fine in **small** apps.""",
        [
            ex(
                "Unidirectional contrast",
                "text",
        """Action -> store -> view is easier to log than A changed B, B changed C, C rewrites A in tight loops.""",
                "Gives a mental picture the interviewer will recognize.",
            )
        ],
        "Do not **bash** a framework; describe **scales and complexity** where unidirectional help matters.",
        "React: sharing state (concept)",
        "https://react.dev/learn/managing-state",
    ),
    item(
        110,
        "Are there any similarities between Redux and RxJS?",
        "intermediate",
        "state-management",
        ["redux", "rxjs", "streams"],
        """Both can model **change over time** and encourage **composable, explicit flows**. **RxJS** is a full **reactive** library of **observables**; **Redux** is a **synchronous, discrete event/reduce** loop with a **single store** snapshot.

**redux-observable** and similar bridges **turn actions into streams** and let you `mergeMap` side effects, which feels **very Rx**. Also **thunks** or **sagas** can look **pipeline-like** like operators, but they are not the same abstraction.

**Net:** you might **embed** **Rx** *inside* middleware or use **Epics**; Redux itself is not an observable, yet **data flow** thinking overlaps.""",
        [
            ex(
                "epic (idea)",
                "ts",
        """// ofType('PING') -> mapTo({type:'PONG'}) in redux-observable""",
                "This is a taste of the overlap without deep Rx interview drilling.",
            )
        ],
        "If the interviewer is deep on **RxJS**, you can name **epics, subjects**; otherwise keep it high level.",
        "redux-observable",
        "https://redux-observable.js.org/",
    ),
    item(
        111,
        "How do you reset state in Redux?",
        "intermediate",
        "state-management",
        ["redux", "reset", "root"],
        """Common options:

- **Root reducer** handles a `RESET` action and returns a **new initial** state object (or nested slices reset in combined reducers with **slice reducers** checking that action if you have cross-slice control).
- **RTK** users often **`configureStore` with a root reducer** that delegates to a **`combineReducers`** result, then a **dedicated** action toggles a **rebuilt** `initial` reference (careful: **slices** may keep private initial state; consider **`extraReducers` listening to `RESET`**).
- **Persist** libraries: **Purge and rehydrate** when logging out, not `window.location.reload` (unless a hard reset is acceptable for security).

Testing often calls **`store.dispatch({ type: 'RESET' })` after a scenario** with a test store""",
        [
            ex(
                "Root reset sketch",
                "ts",
        """function root(s = initial, a) {\n  if (a.type === 'LOGOUT/RESET') return initial; // re-run combineReducers on fresh\n  // else combined flow\n  return appReducer(s, a);\n}\n""",
                "The exact form depends on whether you have RTK or classic combineReducers.",
            )
        ],
        "Mention you **wipe** sensitive data on logout, not just UI route changes.",
        "Redux FAQ: how to implement logout",
        "https://redux.js.org/faq/implementation#how-do-i-combine-a-logoutreducer--reset-action-that-returns-the-initial-state",
    ),
    item(
        112,
        "What is the difference between React Context and React Redux?",
        "intermediate",
        "state-management",
        ["context", "react-redux", "performance"],
        """**Context** is a **built-in React** mechanism to pass a **value** through the tree without prop drilling, while **Redux** is a **dedicated** global store and pattern with **middleware, time travel, and devtools** and **connect/useSelector** subscription optimizations.

**Context** re-renders **all** consumers of that `Provider` when the **value identity** changes, unless you **split** contexts and **memo** carefully. **Redux** uses a **refined subscription** model: components **only** re-run when the **selected state slice** changes, using **memoized selectors** and `useSelector` with equality.

Use **Context** for **stable** or **rare** updates (theme, locale, a narrow API client), and **Redux/RTK** for **frequent, complex, cross-cutting** app state, or a **query cache** (RTK Query) for server state.""",
        [
            ex(
                "useSelector vs useContext (idea)",
                "tsx",
        """// useContext(ThemeContext) re-renders on any new object reference from Provider\n// useSelector(s => s.ui.theme) re-renders when `theme` changes per equality fn\n""",
                "In interviews, the performance difference is a classic answer.",
            )
        ],
        "Avoid putting **a huge, ever-shifting object in one Context** at app root; it is a common perf foot-gun.",
        "React: Context",
        "https://react.dev/reference/react/createContext",
    ),
    item(
        113,
        "Why are Redux state functions called reducers?",
        "beginner",
        "state-management",
        ["reducer", "fold", "pure"],
        """The name comes from **Array.prototype.reduce (fold)**: a **reducer** is a function that **combines** an **accumulator** (previous `state`) with the current **value** (here, an `action`) to get the next accumulator **deterministically**.

A Redux reducer is exactly that: **`state = f(state, action)`** for each dispatched action, producing the **new state snapshot**. The **purity** matches **functional** fold/reduce in FP literature.""",
        [
            ex(
                "Array reduce analogy",
                "ts",
        """const s = [1,2,3].reduce((a, n) => a + n, 0); // 6, fold stepwise\n""",
                "The mental model: repeated fold over an action log (conceptually) though Redux applies one at a time live.",
            )
        ],
        "Mention the **reducer** name also appears in `Array.reduce` in MDN, which is expected in interviews.",
        "MDN: Array.prototype.reduce",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce",
    ),
    item(
        114,
        "How do you make an AJAX request in Redux?",
        "intermediate",
        "state-management",
        ["redux", "thunk", "async"],
        """You do **not** do raw XHR in a **reducer**. Instead, use **asynchronous** layers:

- **Redux Thunk:** `() => (dispatch) => { fetch... then dispatch }`.
- **RTK `createAsyncThunk`** or `createListenerMiddleware` in modern code.
- **RTK Query** for HTTP caching, invalidation, and dedupe.
- **Sagas** (generator-based) in older or complex orchestration.

The **thunk (or side-effect middleware)** **dispatches** **pending/fulfilled/rejected** actions; **reducers** only update for those **plain** actions, keeping async **out of** the pure function.""",
        [
            ex(
                "createAsyncThunk shape",
        "ts",
        """import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';\n\ntype User = { id: string };\n\nexport const loadUser = createAsyncThunk('user/load', (id: string) =>\n  fetch(`/api/u/${id}`).then((r) => r.json() as Promise<User>)\n);\n\nconst userSlice = createSlice({\n  name: 'user',\n  initialState: { data: null as User | null, status: 'idle' as 'idle' | 'loading' | 'succeeded' },\n  reducers: {},\n  extraReducers: b =>\n    b\n      .addCase(loadUser.pending, s => { s.status = 'loading'; })\n      .addCase(loadUser.fulfilled, (s, a) => {\n        s.status = 'succeeded';\n        s.data = a.payload;\n      }),\n});\n""",
                "Simplified sketch; the point is: async in thunk, not reducer.",
            )
        ],
        "If the app is mostly server data, mention **RTK Query** to avoid hand-written fetch boilerplate.",
        "Redux Toolkit: createAsyncThunk",
        "https://redux.js.org/usage/usage-with-typescript#createasyncthunk",
    ),
    item(
        115,
        "Should you keep all component states in the Redux store?",
        "intermediate",
        "state-management",
        ["redux", "local-state", "duplication"],
        """**No.** **Local, ephemeral** UI (open/closed, input scratch text before submit, focus, hover) usually belongs in **`useState`**, **`useReducer`**, or a **form library** to avoid noisy global actions. **Server cache** is often a better fit for **RTK Query**, **TanStack Query**, or **SWR** than copying everything into a client store.

Put **in Redux (or a global model)** the state that is **read by many distant components**, that must be **replayed or debugged**, or is **the user's canonical client session** for the app. Otherwise you **bloat the store, slow re-renders, and complicate** tests.

A nice rule: **if losing it on full refresh is fine** and it is not shared, it is a **strong signal** for local state first.""",
        [
            ex(
                "example split",
        "text",
        """Modal 'open' local; authenticated user + cart in global / query cache.\n""",
                "Helps the interviewer see judgment, not dogma.",
            )
        ],
        "Mention that **form drafts** in Redux-Form/RTK is older style; RHF+server cache is a modern split.",
        "Redux: Organizing state",
        "https://redux.js.org/style-guide/#structure-files-as-feature-folders-or-ducks",
    ),
    item(
        116,
        "What is the proper way to access the Redux store?",
        "intermediate",
        "state-management",
        ["useSelector", "react-redux", "connect"],
        """**From React:** **`useSelector` with a selector** (optionally from **reselect**) or the legacy **`connect` mapState** path. The **Provider** at the app root is required so hooks resolve the store. Avoid reading **`store` directly** in components; you lose **subscription and batched** updates the hooks give you.

**Outside React:** the exported **`store` reference** in narrow cases (as noted earlier). In tests, you may also **`render` with a custom** **`<Provider store={s}>`**.

**TypeScript:** add **`useAppDispatch` and `useAppSelector` wrapper types** to keep dispatch/enhanced store typing tight.""",
        [
            ex(
                "typed hooks",
        "ts",
        """import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';\nimport { AppDispatch, RootState } from './store';\n\nexport const useAppDispatch: () => AppDispatch = useDispatch;\nexport const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;\n""",
                "Redux docs show this as the default TS pattern in template apps.",
            )
        ],
        "Repeat: **useSelector, not** `getState` in most components, for reactivity.",
        "useSelector: React Redux",
        "https://react-redux.js.org/api/hooks#useselector",
    ),
    item(
        117,
        "What is the difference between a component and a container in React Redux?",
        "intermediate",
        "state-management",
        ["container", "presentational", "separation"],
        """Historically, **presentational** (dumb) **components** received **data and callbacks** via **props** and were easy to test visually, while **container** (smart) **components** used **`connect`** to select state and bind dispatch to props.

**Hooks** blurred the line: you often have **a single function component** that both **uses `useSelector`** and **renders markup**. The **separation of concerns** still helps when you colocate a **view-only** subcomponent, but the **naming** "container" is less used today.

In interviews, describe **smart vs presentational** as a **separation of Redux wiring and UI**, not as two file types you must have.""",
        [
            ex(
                "Refactor to dumb child",
        "tsx",
        """function CountView({ n, onInc }: { n: number; onInc: () => void }) {\n  return <button onClick={onInc}>{n}</button>;\n}\n\nexport function CountBox() {\n  const n = useAppSelector(s => s.c.n);\n  const d = useAppDispatch();\n  return <CountView n={n} onInc={() => d(inc())} />;\n}\n""",
                "The inner component stays pure and is easy to snapshot-test.",
            )
        ],
        "Be modern: the **useSelector+props** factoring still carries the old container idea.",
        "Redux: Usage with React: hooks",
        "https://react-redux.js.org/api/hooks",
    ),
    item(
        118,
        "What is the purpose of constants in Redux?",
        "intermediate",
        "state-management",
        ["actions", "constants", "typos"],
        """**String literal action `type` fields** used to be easy to **mis-spell** across files, so teams centralized **`const ADD_TODO = 'ADD_TODO' as const`** in a module and imported it everywhere, letting **TypeScript and editors** help.

**Redux Toolkit's `createSlice` auto-generates** `slice.actions.addTodo` with a stable string type, so **raw string constants** are **less** central than in the **pre-RTK** era. The purpose remains: **one canonical type string** and **exhaustive** handler checks, sometimes with a **`type Action = ...` union** for reducers in TS.

**Net:** **avoid drifts in action names and enable tooling**; RTK just moved where that name lives (inside the slice).""",
        [
            ex(
                "as const module",
        "ts",
        """export const T = { add: 'todos/add' as const, del: 'todos/del' as const };\n""",
                "A manual pattern; RTK slices emit similar strings automatically under the hood.",
            )
        ],
        "If the interviewer is legacy-focused, they want **`ActionTypes` files**; if modern, you mention **createSlice**.",
        "Redux Toolkit: createSlice",
        "https://redux.js.org/usage/usage-guide/#slices-and-the-createSlice-function",
    ),
    item(
        119,
        "What are the different ways to write mapDispatchToProps()?",
        "intermediate",
        "state-management",
        ["mapdispatch", "connect", "bindactioncreators"],
        """- **`Object` form:** pass **`{ doThing: doThingActionCreator }`**, and **react-redux** uses **`bindActionCreators`**.

- **Function** form: **`(dispatch) => ({ doThing: () => dispatch(doit()) })`** for more control, including **closures** and **`ownProps`**: **`(dispatch, ownProps) =>`**.

- **`null` or omitted:** you only get `dispatch` manually if you return nothing from mapDispatch, depending on version—usually you **intentionally** provide one of the first two to inject bound creators.

**Hooks** replace this with **`const dispatch = useDispatch()` and `dispatch(doit())` or** bound helpers from slice actions.""",
        [
            ex(
                "Function form (idea)",
        "ts",
        """const mapD = (d: AppDispatch) => ({\n  onSave: (id: string) => d(saveRequested(id)),\n});\n""",
                "Gives a taste of the flexibility when you need `ownProps` in older code.",
            )
        ],
        "Name **`bindActionCreators`** for completeness in legacy `connect` interviews.",
        "bindActionCreators: Redux",
        "https://redux.js.org/api/bindactioncreators",
    ),
    item(
        120,
        "What is the use of the ownProps parameter in mapStateToProps() and mapDispatchToProps()?",
        "intermediate",
        "state-management",
        ["ownprops", "connect", "routing"],
        """**`ownProps` are the same props the **wrapped** component would receive from its **parent** (for example a router **`match.params.id`** in older HOCs). Mappers that take **`(state, ownProps)`** let you **select** store fields **in terms of a route param** or a **parent prop** without the child passing them twice.

A classic example: **`mapState: (s, p) => ({ item: s.items[p.match.params.id] })`** in v4 routing.

With **hooks + TypeScript** you can **read params with `useParams` directly** in the component and `useSelector` in the same function, so explicit `ownProps` is rarer, but the **interview** still checks that you know **per-instance selection** is sometimes needed.

You must **return referentially stable** objects with care, or you may cause **extra re-renders** (use memoized factory selectors, `reselect`).""",
        [
            ex(
                "reselect (mention)",
        "ts",
        """import { createSelector } from '@reduxjs/toolkit';\n// selectItemById = createSelector([(s) => s.items, (_, id: string) => id], (m, id) => m[id]);\n""",
                "Combining `ownProps` with `createSelector` is a performance-safe pattern in connected components.",
            )
        ],
        "When using legacy **connect** with `ownProps`, watch **selector re-creates** per render; factory selectors are the fix.",
        "reselect: createSelector",
        "https://redux.js.org/usage/deriving-data-selectors#createselector--createselectormemoinputselectors-memoizeselector-",
    ),
    item(
        121,
        "How do you structure Redux top-level directories?",
        "intermediate",
        "state-management",
        ["structure", "ducks", "rtk"],
        """**Feature folders / slices (ducks)**: one folder per feature with `slice.ts`, `selectors`, and maybe **components** (colocated) is the **current Redux style guide** default with **RTK**. Keep **`store.ts`**, **typed hooks**, and **root reducer** at `app/` or `state/`.

Alternatives in older codebases: **separate** `reducers/`, `actions/`, and `types/`; good for very large orgs, but it **scatters** a feature. **Colocate tests** and **mocks** next to the slice.

**Do not** over-nest; **3–5 top-level** folders under `src` are easier to scan than 12 tiny buckets. When using **Next.js**, **server and client** modules must be separated to avoid **accidentally importing a Node-only** module into a client bundle, which affects how you place **store** files.""",
        [
            ex(
                "Feature folder sketch",
        "text",
        """src/features/cart { cartSlice.ts, cartSelectors.ts, CartPanel.tsx, cartAPI.ts }\n""",
                "A slice-first layout matches the official style guide in spirit.",
            )
        ],
        "Mention the **Redux style guide** by name: **feature colocation, avoid barrel-file cycles**.",
        "Redux: Style guide",
        "https://redux.js.org/style-guide/",
    ),
    item(
        122,
        "What is Redux Saga?",
        "intermediate",
        "state-management",
        ["redux-saga", "generators", "side-effects"],
        """**Redux-Saga** is a **side-effect** middleware for Redux that uses **ES generator functions** to **describe** async flows as a **saga** that can **wait on** actions with `take`, and **put** new ones with `put`. It is **imperative-looking but structured** in `yield` steps.

You get **cancellable** tasks, **concurrency patterns** (`takeLatest` vs `takeEvery`, `race`, `debounce` helpers) and a **separate** place from components for **I/O and orchestration**, compared to **thunk**'s `async` style.

**Tradeoffs:** some teams find **generators and testing sagas** heavier than `async/await` thunks, while **large orchestrations** (multi-step wizards) can be clearer in sagas. **Adoption in new apps** is mixed with **RTK Query** and **thunks** taking common paths.""",
        [
            ex(
                "put/take (names only)",
        "ts",
        """import { put, takeEvery } from 'redux-saga/effects';\n// function* watch() { yield takeEvery('PING', function* p() { yield put({ type: 'PONG' }); }); }\n""",
                "The interview will often name **effect helpers**; exact imports vary by version.",
            )
        ],
        "Differentiate from **thunks**: **long-running watchers** are a **saga strength**; keep answers practical.",
        "redux-saga: doc",
        "https://redux-saga.js.org/docs/introduction/GettingStarted",
    ),
    item(
        123,
        "What is the mental model of Redux Saga?",
        "intermediate",
        "state-management",
        ["redux-saga", "generators", "orchestration"],
        """Think of a **saga** as a **process manager** in the background that **listens to an action stream** and **yields** **effects** (objects describing work) instead of doing it inline. The **middleware** executes those **effects** (I/O) and **resumes** the generator when the result arrives.

Mental model: **action in -> side effect** out as **another** action, while **reducers** stay **pure** for state shape. The **`yield*`-style** flow reads like **a script** of steps with **cancellable** points.

Compare to a **thunk** where the **function returns a Promise**; in **saga**, the **interpreter** is always there between yields.""",
        [
            ex(
                "Effect vs work",
        "text",
        """`put` and `call` are **descriptions**; middleware performs them, keeping reducers test-pure in spirit.""",
                "A crisp distinction the interviewer can nod at.",
            )
        ],
        "You can mention **'interpreter'** and **'effect description'**; it signals depth without 10 minutes of code.",
        "redux-saga: beginner tutorial",
        "https://redux-saga.js.org/docs/introduction/BeginnerTutorial",
    ),
    item(
        124,
        "What are the differences between call and put in Redux Saga?",
        "intermediate",
        "state-management",
        ["call", "put", "effects"],
        """**`call` runs (or **describes** running) a function** or a **promise-returning** call and **suspends the saga** until the result returns. It is the safe way to **call APIs** and keep those invocations **testable and mockable** in saga tests (you can `expect(gen.next().value).toEqual(call(fn)))` in older patterns).

**`put` dispatches an action to the store**; it is like **`dispatch`**, and can **fan out** follow-up work that reducers and other sagas can react to.

**Rule of thumb**:** `call` = **do a thing, get a value**; `put` = **tell the app something happened** as the **Redux** action event stream. Both return **effect objects** to the **middleware** interpreter.""",
        [
            ex(
                "api flow",
        "ts",
        """// const u = yield call(api.fetchUser, id); yield put(userLoaded(u));\n""",
                "The sequence keeps async out of the reducer, actions explicit.",
            )
        ],
        "Clarify **`call` can wrap promises or sync functions**; `put` always targets the **Redux** dispatch pipeline.",
        "Effect creators: call / put",
        "https://redux-saga.js.org/docs/api#callfn-args",
    ),
    item(
        125,
        "What is Redux Thunk?",
        "intermediate",
        "state-management",
        ["redux-thunk", "async", "middleware"],
        """**Redux-Thunk** is the **default async middleware** in many Redux setups. It lets you **dispatch a function** instead of a plain action object, and that function receives `(dispatch, getState)` to **orchestrate** **multiple** sync dispatches, **async/await** calls, and **guards** before dispatching.

**RTK** includes **thunk** support out of the box, and you still write `createAsyncThunk` which **builds** on the same model under the hood. **TypeScript** can type **`ThunkDispatch`**.

**Contrast with saga:** a thunk is often **a single** async function with straightforward **Promise** logic; a saga can be a **long watcher** with more advanced concurrency, but the **cognitive** load differs across teams.

Thunks are **adequate** for most CRUD apps, especially with **error handling and conditional `dispatch`**.""",
        [
            ex(
                "inline thunk (idea)",
        "ts",
        """const f = (id: string) => async (d: AppDispatch) => {\n  d(loading());\n  try {\n    const u = await api(id);\n    d(loaded(u));\n  } catch (e) {\n    d(failed(e));\n  }\n};\n""",
                "Classic pattern before RTK's createAsyncThunk.",
            )
        ],
        "State **'thunk' means a function in dispatch**' for historical quiz questions.",
        "Redux: Writing logic with thunks",
        "https://redux.js.org/usage/writing-logic-thunks#writing-thunks-with-createrequestasync",
    ),
    item(
        126,
        "What are the differences between Redux Saga and Redux Thunk?",
        "intermediate",
        "state-management",
        ["saga", "thunk", "compare"],
        """**Sagas** use **generators and an effect model**; **thunks** use **async functions and dispatch**. Sagas are **strong** at **concurrency** (`takeLatest` vs `takeEvery` built-in) and **long-running** coordination; thunks are **simpler** and familiar to any dev who knows `async/await`.

**Test story:** people either **mock** fetches in both, or in sagas they **assert yielded effects**; both have tradeoffs. **Bundle size and learning** curve favor thunks; **sagas** add **a framework** in your middleware.

**Modern:** many apps **reduce** the need for either by using **RTK Query** for data fetching and a **thunk** only for the odd one-off, while **Sagas** remain in some large enterprise UIs and admin consoles.""",
        [
            ex(
                "When saga wins",
        "text",
        """Cancellation of in-flight fetches and race conditions between rapid tab changes can be neater in sagas with `takeLatest`/`race`.""",
                "A concrete differentiator, not a slogan.",
            )
        ],
        "Avoid saying one is *always* better; **show you pick by workflow complexity and team experience**.",
        "When should I use a thunk vs saga? (StackOverflow pattern)",
        "https://redux.js.org/usage/side-effect-approaches",
    ),
    item(
        127,
        "What is Redux DevTools?",
        "beginner",
        "tooling",
        ["redux-devtools", "browser", "time-travel"],
        """**Redux DevTools** is a **browser** extension and optional **local server** that **connects to your Redux `store`**, **logs actions**, and lets you **inspect state, diff changes, and jump through time** by replaying actions.

`configureStore` with the **default** dev flag wires it in **development**; you can **serialize** and **filter** some noisy actions, and in production you usually **turn it off** for bundle and safety reasons.

**RTK and RTK Query** work well with the same **devtools**; it is a **key reason** teams adopt Redux: **transparency in prod debugging** in controlled environments, or in **reproducible** support sessions when allowed.""",
        [
            ex(
                "dev-only enable",
        "ts",
        """const store = configureStore({ reducer, devTools: process.env.NODE_ENV !== 'production' });\n""",
                "Common guard to avoid shipping devtools in prod bundles.",
            )
        ],
        "Mention **action sanitization and max age** in huge apps; devtools can **freeze** if the state is enormous.",
        "Redux DevTools Extension",
        "https://github.com/reduxjs/redux-devtools",
    ),
    item(
        128,
        "What are the features of Redux DevTools?",
        "intermediate",
        "tooling",
        ["redux-devtools", "time-travel", "export"],
        """Common features: **action log with timestamps, state inspection per action, time-travel to previous state, diffing**, **custom** action creators logging, and **import/export of action/state sessions** to share a bug in Slack.

**Remote** (legacy setups) can stream **to a custom monitor**; most teams use the **Chrome** extension. **Lock-up** and **state size** are practical limits; for large state you **use selectors** in the view or **filter** displayed slices.

**TypeScript** users benefit from **typed** actions when logging; **reselect** helps keep **view** of huge trees narrow.""",
        [
            ex(
                "export session",
        "text",
        """Export JSON of actions + state to replay in another machine with the same reducer code to reproduce a support ticket.""",
                "A selling point in enterprise support workflows.",
            )
        ],
        "Connect **replay** to **pure reducers and serializable** actions, which is non-optional for strong devtools use.",
        "Redux DevTools: features",
        "https://github.com/reduxjs/redux-devtools/blob/main/docs/Walkthrough.md",
    ),
    item(
        129,
        "What are Redux selectors and why should you use them?",
        "intermediate",
        "state-management",
        ["reselect", "selectors", "derived"],
        """**Selectors** are functions **`(state) => data`** that **derive** view-model fields from the **raw store** (filter, join, map). You should use them to **encapsulate** the shape of `state`, avoid **recomputing** heavy joins on every render, and **test** the derivation separately from the components.

**`createSelector`** (Reselect) **memoizes** by **input** references so the output object stays referentially **stable** when inputs have not changed, which helps **`React.memo` and `useSelector` equality checks**.

**RTK** includes **reselect** so you can build slice-local selectors. **Over-selecting in components** (big inline lambdas) can cause more **re-renders** than you expect without memoization.""",
        [
            ex(
                "createSelector",
        "ts",
        """import { createSelector } from '@reduxjs/toolkit';\nconst selectC = (s: Root) => s.cart;\nconst selectTotal = createSelector([selectC], c =>\n  c.items.reduce((n, l) => n + l.qty * l.price, 0)\n);\n""",
                "Only recomputes when `c` identity changes, not when unrelated state updates happen.",
            )
        ],
        "Say **'derived data in selectors'** to echo React docs about keeping render cheap and dumb.",
        "Reselect: createSelector",
        "https://redux.js.org/usage/deriving-data-selectors#createselector",
    ),
    item(
        130,
        "What is Redux Form?",
        "intermediate",
        "forms",
        ["redux-form", "legacy", "field"],
        """**Redux-Form** is a **HOC/field** library that stores each field's value and meta **in Redux state** and synchronizes with inputs. In **older** codebases, it integrated tightly with `react-redux` and gave **synchronous and async** validation, **touched/visited** flags, and `change` **actions** for every keystroke in some models.

**Today** the project is **maintenance mode**; new apps usually choose **React Hook Form** or **Formik** with local state (or a dedicated server schema layer), because **every keystroke to Redux** can be **noisy and heavy**. **RTK** does not push you to Redux-Form for new apps.

**Interview:** explain **pro** (all form state in one time-traveling store) vs **con** (perf and boilerplate) vs **RHF** local models.""",
        [
            ex(
                "RHF note",
        "tsx",
        """// Modern default pattern\n// const { register, handleSubmit } = useForm<Schema>();\n""",
                "Shows you are up to date beyond legacy Redux-Form years.",
            )
        ],
        "If a job **still** uses it, you say you are comfortable reading **`reduxForm` HOCs**; not that you would pick it for a green field.",
        "redux-form: repo status",
        "https://github.com/redux-form/redux-form",
    ),
    item(
        131,
        "What are the main features of Redux Form?",
        "intermediate",
        "forms",
        ["redux-form", "validation", "fields"],
        """Headline **features:** **`Field` / `FieldArray`**, **sync and async** validation functions, **initialValues**, **`enableReinitialize`**, **normalizing** and **pluggable** `reducer` for form state per form key, and **action creators** to imperatively `change` or `autofill` a field from sagas or thunks.

**Meta** fields like **`pristine`**, `dirty`, **submitting**, and **error** on fields support UX feedback. The cost is a **sizable** chunk of the store for large forms, and a **lot** of re-renders if you do not `shouldValidate` and **memo** carefully in older versions.

In modern work you map these needs to **RHF** + **Zod** + **isDirty/touched** props instead, unless you are maintaining a legacy app.""",
        [
            ex(
                "FieldArray (concept)",
        "text",
        """Dynamic list rows in a form with per-row validation, stored as nested form state in Redux-Form's slice of the big tree.\n""",
                "A classic interview question about *why* companies moved to local form state in component trees.",
            )
        ],
        "Be ready to name **`initialValues` vs reinitialize** and stale server loads from earlier questions in this set.",
        "Redux Form: Field (archive)",
        "https://redux-form.com/8.3.0/docs/api/field/",
    ),
    item(
        132,
        "How do you add multiple middlewares to Redux?",
        "intermediate",
        "state-management",
        ["middleware", "store", "applymiddleware"],
        """Pass an **array of middlewares** to **`configureStore` ({ middleware: getDefault => ...})`** in RTK, which **composes** them with **`applyMiddleware`** in the right order. Historically, **`createStore` + `applyMiddleware(thunk, logger, saga)`** did the same.

**Order** matters: **thunk** is usually **before** action-transforming or logging, **sagas** are a single middleware, and **immutability checkers** are dev-only. **Preloaded state** and **enhancers** are separate; still pass **a composed `composeWithDevTools(applyMiddleware(...))` enhancer in classic APIs**.

**RTK** `getDefaultMiddleware` **includes thunk** and a **dev immutability** check in dev; you **customize** with **callbacks** that **prepend/append** and **turn off** checks as needed in tests.""",
        [
            ex(
                "getDefaultMiddleware customize",
        "ts",
        """configureStore({\n  reducer,\n  middleware: (g) =>\n    g().concat(myApi.middleware /* RTK Q */, logger as const),\n});\n""",
                "This is a typical RTK+Query setup pattern.",
            )
        ],
        "Name **synchronous vs async** ordering: a logger after thunk sees the **thunk** output actions too.",
        "Redux: applyMiddleware",
        "https://redux.js.org/api/applymiddleware",
    ),
    item(
        133,
        "How do you set the initial state in Redux?",
        "beginner",
        "state-management",
        ["initial-state", "reducer", "preloaded"],
        """**Reducers** each export their **`initialState`** in **`createSlice`**, and **`configureStore` can take `preloadedState`** to **hydrate** the store from the server, storage, or a fixture in tests. The **reducer** `initialState` is the **default** if no preloaded is passed.

**Classic** `createStore` took **`preloadedState` as the second** argument. **State rehydration** in SSR: **serialize the server snapshot** to JSON and `createStore` on the **client** with the same preloaded, **beware of Date** and **class** instances, only **plain** JSON-safe data in global serial flows.

**Migration:** when the **schema** changes, use **a migration** step or **rehydrate a compatible** subset and **re-fetch** the rest, not a blind `localStorage` parse.""",
        [
            ex(
                "preloaded with RTK",
        "ts",
        """const store = configureStore({ reducer, preloadedState: { user: { name: 'anon' } } });\n""",
                "Tests often create tiny inline preloaded for scenario-specific stores.",
            )
        ],
        "Pair with **persistence** libraries that **version** the blob you load into `preloadedState`.",
        "Redux: createStore (legacy)",
        "https://redux.js.org/legacy/createstore#arguments",
    ),
    item(
        134,
        "How is Relay different from Redux?",
        "intermediate",
        "data-fetching",
        ["relay", "graphql", "redux"],
        """**Relay** is a **GraphQL-** oriented **data framework** for **React** that **caches and normalizes** server data with **a compiler** that **pulls in fragments, variables, and types**. It is **tightly coupled to GraphQL** and **excellent** in large orgs on a **schema-first** model.

**Redux** is a **client state** library **agnostic to transport**; you can put **anything** in the tree and fetch with ad hoc fetches, **thunks**, or **RTK Query** for **REST/GraphQL**.

**Intersection:** you can have **Redux** for some UI session state and **Relay** for a **server cache**, but they solve **different** primary problems. If you are **all-in** on GraphQL with a mature pipeline, **Relay (or URQL+normalized cache) vs RTK Query** is the trade conversation.

**Mental line:** **Redux: explicit global client store**, **Relay: GraphQL colocated components + normalized cache and GC**.""",
        [
            ex(
                "Query component idea",
        "text",
        """Relay's `useFragment` ties UI pieces to a normalized record id in a shared store, unlike hand-written reducer maps that mirror REST shapes manually.\n""",
                "Useful contrast for senior interview panels.",
            )
        ],
        "Mention the **Relay compiler** step, which is a different kind of 'tooling' than a dumb Redux file tree.",
        "Relay: documentation",
        "https://relay.dev/docs/",
    ),
    item(
        135,
        "What is an action in Redux?",
        "beginner",
        "state-management",
        ["action", "dispatch", "plain-object"],
        """An **action** is a **plain JavaScript object** (JSON-serializable in spirit) with a **required `type: string` field** that tells reducers *what* happened, plus **optional** payload fields you define by convention, often in **`payload`** with **RTK** slices' generated creators.

**Actions are the only** way **state** should change, except **`STORE_INIT`** style hacks in advanced patterns. The **reducer** pattern matches the action `type` in a `switch` or `builder.addCase` and returns a **new** state or the old reference if nothing applies.

**Async** flows end up as **plain actions** for success/fail after middleware turns network results into `dispatch` calls.""",
        [
            ex(
                "action object (classic)",
        "ts",
        """type A =\n  | { type: 'todos/toggle'; id: string }\n  | { type: 'todos/add'; text: string };\n// dispatch action -> reducer case handles the union with narrowing\n""",
                "In TypeScript, a discriminated union on `type` is common.",
            )
        ],
        "Say `createAction` and **RTK** hide string duplication, but the **type string** is still the spine of the event log.",
        "Redux: Actions",
        "https://redux.js.org/understanding/thinking-in-redux/three-principles#changes-are-made-with-pure-reducers-2",
    ),
]

# --- chunk 208-300 (user Q 227-319) ---

_ch2_path = Path(__file__).resolve().parent / "emit_react_ch2_data.py"
_ch2_spec = importlib.util.spec_from_file_location("emit_react_ch2_data", _ch2_path)
_ch2_mod = importlib.util.module_from_spec(_ch2_spec)
assert _ch2_spec.loader
_ch2_spec.loader.exec_module(_ch2_mod)
CH2: list = _ch2_mod.build_ch2(item, ex)

ROOT = Path(__file__).resolve().parent.parent / "content" / "modules" / "react"


def main() -> None:
    (ROOT / "chunk_079_135.json").write_text(
        json.dumps(CH1, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    (ROOT / "chunk_208_300.json").write_text(
        json.dumps(CH2, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
