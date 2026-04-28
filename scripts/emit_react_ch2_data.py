# -*- coding: utf-8 -*-
"""Build react-208..300 (user Q 227-319) using shared templates + per-row links."""

# (id, question, diff, category, (tag1, tag2, tag3), link_key, tpl)
TABLE: list = []


def _load_table() -> None:
    global TABLE
    T = "intermediate"
    B = "beginner"
    A = "advanced"
    TABLE = [
        (208, "What is MobX?", T, "state-management", ("mobx", "reactive", "observables"), "mobx", "t_mobx"),
        (209, "What are the key differences between Redux and MobX?", T, "state-management", ("redux", "mobx", "contrast"), "redux", "t_state"),
        (210, "Should you learn modern JavaScript (ES6+) before React?", B, "javascript", ("es6", "learning", "fundamentals"), "mdn", "t_js"),
        (211, "What is concurrent rendering in React?", A, "rendering", ("concurrent", "fiber", "scheduler"), "react", "t_conc"),
        (212, "What is the difference between the older 'async mode' and concurrent features in React?", A, "rendering", ("async-mode", "concurrent", "history"), "react", "t_conc"),
        (213, "What changed in React 16.9 regarding deprecated JavaScript URLs in DOM attributes?", T, "security", ("xss", "javascript-urls", "dom"), "react", "t_sec"),
        (214, "What does the official ESLint plugin for React Hooks enforce?", T, "tooling", ("eslint", "hooks", "exhaustive-deps"), "eslint", "t_lint"),
        (215, "What is the difference between imperative and declarative React code?", B, "fundamentals", ("declarative", "imperative", "ui"), "react", "t_style"),
        (216, "What are the main benefits of using TypeScript with React?", T, "types", ("typescript", "safety", "refactor"), "ts", "t_ts"),
        (217, "How can you share an authentication session and implement token refresh using React context?", T, "auth", ("auth", "context", "refresh"), "react", "t_auth"),
        (218, "What are the main benefits of the new JSX transform?", T, "build", ("jsx-transform", "babel", "runtime"), "react", "t_jsx"),
        (219, "How does the new JSX transform differ from the classic `React.createElement` style?", T, "build", ("createelement", "import-jsx", "runtime"), "react", "t_jsx"),
        (220, "What are React Server Components (RSC)?", A, "server-components", ("rsc", "server", "client"), "react", "t_rsc"),
        (221, "What is prop drilling, and when is it a problem?", B, "state", ("props", "composition", "context"), "react", "t_props"),
        (222, "When do you use useState versus useRef in function components?", T, "hooks", ("usestate", "useref", "render"), "react", "t_hookpair"),
        (223, "What is a wrapper (or HOC) component pattern, and when is it useful?", T, "patterns", ("hoc", "wrapper", "composition"), "react", "t_pattern"),
        (224, "What is the difference between useEffect and useLayoutEffect?", T, "hooks", ("useeffect", "uselayout", "dom"), "react", "t_effect"),
        (225, "How do functional and class components differ in modern React?", T, "components", ("classes", "hooks", "legacy"), "react", "t_class"),
        (226, "What is React Strict Mode?", B, "strict-mode", ("strict", "dev", "double-invoke"), "react", "t_strict1"),
        (227, "What is the main benefit of enabling Strict Mode during development?", B, "strict-mode", ("side-effects", "purity", "dev"), "react", "t_strict1"),
        (228, "Why can Strict Mode intentionally double-render components in development?", T, "strict-mode", ("double-render", "development", "bugs"), "react", "t_strict1"),
        (229, "What are the core rules of writing JSX in React?", B, "jsx", ("rules", "expressions", "return"), "react", "t_jsxrules"),
        (230, "How do you return multiple root elements in JSX, and what wrap do you use?", B, "jsx", ("fragment", "keys", "return"), "react", "t_jsxrules"),
        (231, "How do you update lists in useState without mutating the array in place?", T, "state", ("immutability", "arrays", "setstate"), "react", "t_immut"),
        (232, "What is the capture phase in the DOM event model, and can React set capture listeners?", T, "events", ("capture", "bubbling", "synthetic"), "mdn", "t_dom"),
        (233, "At a high level, how does React update the screen after a state change?", T, "reconciliation", ("fiber", "reconcile", "commit"), "react", "t_recon"),
        (234, "What is state update batching in React?", T, "batching", ("batching", "setstate", "react18"), "react", "t_batch"),
        (235, "In older React, how was batching different from React 18 automatic batching in async handlers?", T, "batching", ("react-17", "react-18", "async"), "react", "t_batch"),
        (236, "What is hydration, and when is it used in SSR/SSG React apps?", T, "ssr", ("hydration", "ssr", "ssg"), "react", "t_ssr"),
        (237, "How do you update object state immutably in React?", B, "state", ("object", "spread", "immutability"), "react", "t_immut"),
        (238, "How do you update deeply nested state without direct mutation?", T, "state", ("nested", "immer", "normalization"), "react", "t_immut"),
        (239, "What patterns are common for arrays stored in useState (add/remove/update)?", T, "state", ("arrays", "map-filter", "lists"), "react", "t_immut"),
        (240, "What is Immer, and when is it used with React state updates?", T, "state", ("immer", "draft", "patches"), "redux", "t_immer"),
        (241, "Why do React and Redux style guides favor avoiding direct mutation of state trees?", T, "state", ("mutation", "debugging", "time-travel"), "react", "t_mutfree"),
        (242, "Which array operations are usually preferred in immutable list updates in React state?", B, "state", ("map", "filter", "slice"), "react", "t_immut"),
        (243, "What is the pitfall of defining a nested function component inside another component's body?", T, "patterns", ("perf", "identity", "remount"), "react", "t_inner"),
        (244, "When is a `key` useful for reconciliation even outside a simple `.map` of items?", T, "reconciliation", ("keys", "reset", "identity"), "react", "t_keys"),
        (245, "What are good guidelines for a reducer you pass to useReducer?", T, "hooks", ("reducer", "pure", "actions"), "react", "t_ured"),
        (246, "What is useReducer, and when would you pick it over useState?", T, "hooks", ("usereducer", "usestate", "transitions"), "react", "t_ured"),
        (247, "How does useReducer help with several related state fields in one object?", T, "hooks", ("usereducer", "related-state", "actions"), "react", "t_ured"),
        (248, "How do you use context together with the useContext hook in modern code?", T, "context", ("usecontext", "provider", "subscribe"), "react", "t_ctx"),
        (249, "What are solid use cases for useContext in application architecture (theme, auth, and so on)?", T, "context", ("theme", "auth", "locale"), "react", "t_ctx"),
        (250, "What is the idea of 'client' versus 'server' components in a React RSC model?", A, "server-components", ("rsc", "client", "server"), "react", "t_rsc"),
        (251, "What is the difference between Next.js Pages Router and the App Router at a high level?", T, "nextjs", ("nextjs", "app-router", "pages-router"), "next", "t_next"),
        (252, "What is useMemo, and when should you actually use it (versus fixing real causes of work)?", T, "hooks", ("usememo", "expensive", "deps"), "react", "t_memo"),
        (253, "Can you use Hooks inside a React class component?", B, "hooks", ("classes", "invalid", "refactor"), "react", "t_rules"),
        (254, "What is the useState functional updater, and when is it better than a plain value set?", T, "hooks", ("usestate", "updater", "stale"), "react", "t_upd"),
        (255, "How does a function initializer in useState work, and when do you use it?", T, "hooks", ("lazy-initial", "usestate", "expensive"), "react", "t_upd"),
        (256, "How do you type useState in TypeScript for unions, tuples, and objects?", T, "types", ("typescript", "generics", "usestate"), "ts", "t_ts2"),
        (257, "Is it valid to call useState in only some code paths (conditionally)?", T, "hooks", ("rules-of-hooks", "conditional", "branches"), "react", "t_rules"),
        (258, "Is setState in React 'async', and what does that imply for reading state immediately after set?", T, "hooks", ("batching", "asynchronous", "closures"), "react", "t_async"),
        (259, "At a high level, how can useState be modeled internally in React (hooks list + per-fiber state)?", A, "hooks", ("fiber", "queue", "dispatcher"), "react", "t_int"),
        (260, "Why do teams use useReducer for more complex, action-driven state transitions?", T, "hooks", ("usereducer", "state-machine", "actions"), "react", "t_ured"),
        (261, "What is a simple useReducer example (counter) that clarifies `dispatch`?", B, "hooks", ("usereducer", "example", "dispatch"), "react", "t_ured"),
        (262, "How can useReducer pair with context to make a small client-side 'store' pattern?", T, "hooks", ("usereducer", "context", "provider"), "react", "t_uredctx"),
        (263, "What happens to batched `dispatch` calls on the same tick with useReducer?", T, "hooks", ("usereducer", "batching", "actions"), "react", "t_ured"),
        (264, "Where should side effects and async I/O go when you use useReducer (hint: not inside the reducer)?", T, "hooks", ("side-effects", "useeffect", "thunks"), "react", "t_asyncred"),
        (265, "What is a small but realistic useContext + Provider + consumer example in modern code?", T, "context", ("example", "provider", "value"), "react", "t_ctxex"),
        (266, "How can you structure multiple context providers, and when should you split them?", T, "context", ("split", "performance", "providers"), "react", "t_ctx"),
        (267, "What is a common pitfall when a new `value` object is created every render for context?", T, "context", ("rerender", "usememo", "stability"), "react", "t_ctxp"),
        (268, "What do consumers get if a Provider is missing, or a default is undefined?", T, "context", ("default", "optional", "errors"), "react", "t_ctxp"),
        (269, "What does the `useEffect` dependency array mean, and what does an empty `[]` mean?", T, "hooks", ("dependencies", "useeffect", "stale"), "react", "t_dep"),
        (270, "When are effect setup and cleanup functions run, and when does `cleanup` run between updates?", T, "hooks", ("cleanup", "resubscribe", "deps"), "react", "t_dep"),
        (271, "What is a correct pattern to call an async IIFE or Promise inside useEffect (race-safe)?", T, "hooks", ("async", "useeffect", "aborted"), "react", "t_async2"),
        (272, "Why is splitting logic across multiple `useEffect` calls often better than one giant effect?", T, "hooks", ("separation", "clarity", "deps"), "react", "t_dep"),
        (273, "How can wrong dependencies cause an infinite re-render or effect loop, and what prevents it?", T, "hooks", ("infinite", "stability", "eslint"), "eslint", "t_dep"),
        (274, "What are good useLayoutEffect use cases, and when should you avoid it?", T, "hooks", ("uselayouteffect", "measure", "mutations"), "react", "t_layout"),
        (275, "What is the SSR story for useLayoutEffect (server warning) and the typical workaround?", T, "ssr", ("uselayouteffect", "ssr", "useeffect"), "react", "t_layout2"),
        (276, "When should you avoid useLayoutEffect for business logic (non layout side effects)?", T, "hooks", ("uselayouteffect", "blocking", "separation"), "react", "t_layout"),
        (277, "What is layout thrashing in the browser, and how can batching and layout tools reduce it?", T, "performance", ("layout", "read-write", "dom"), "mdn", "t_perf"),
        (278, "What is a common useRef example for direct DOM access (for example, focusing an input)?", T, "hooks", ("useref", "dom", "imperative"), "react", "t_ref1"),
        (279, "What is the difference between ref-as-instance-variable versus state for mutable values that should not re-render?", T, "hooks", ("useref", "mutable", "stale"), "react", "t_ref1"),
        (280, "How can you keep the previous prop or state value in a function component (ref + effect pattern)?", T, "hooks", ("previous", "useref", "useeffect"), "react", "t_ref2"),
        (281, "What are the caveats of reading and writing to `ref.current` during render versus in effects?", A, "hooks", ("useref", "render", "side-effect"), "react", "t_ref2"),
        (282, "What are the most common production `useRef` use cases (DOM, intervals, and previous values)?", T, "hooks", ("useref", "real-world", "timers"), "react", "t_ref1"),
        (283, "What is useImperativeHandle, and how does it work with `forwardRef`?", T, "hooks", ("useimperativehandle", "forwardref", "imperative"), "react", "t_imph"),
        (284, "When is useImperativeHandle a good design choice, and when should you prefer declarative props?", T, "hooks", ("leaky-abstraction", "api", "components"), "react", "t_imph"),
        (285, "What patterns replace imperative ref wiring when you do not use `forwardRef` (callback refs, composition)?", T, "hooks", ("ref", "callback-ref", "composition"), "react", "t_imph"),
        (286, "What is the difference between useMemo and useCallback (return value vs stable function ref)?", T, "hooks", ("usememo", "usecallback", "identity"), "react", "t_memo2"),
        (287, "When does `useMemo` *not* stop a child from re-rendering, and what else do you need (for example, `memo`)?", T, "hooks", ("memo", "children", "props"), "react", "t_memo2"),
        (288, "What problem does useCallback try to solve for object identity and dependency arrays?", T, "hooks", ("usecallback", "identity", "deps"), "react", "t_memo2"),
        (289, "What is a custom hook, and what naming and Rules-of-Hooks rules apply to it?", T, "hooks", ("custom-hook", "reuse", "rules"), "react", "t_cust"),
        (290, "What is React Fiber at a high, interview-appropriate level?", T, "rendering", ("fiber", "scheduler", "incremental"), "react", "t_fiber"),
        (291, "What is `useId` for, and why is a counter in render not equivalent for accessibility + SSR ids?", T, "hooks", ("useid", "ssr", "a11y"), "react", "t_useid"),
        (292, "What is `useDeferredValue` and when is it a good way to keep typing responsive under heavy work?", T, "hooks", ("deferred", "concurrent", "input"), "react", "t_defer"),
        (293, "How do `useTransition` and `useDeferredValue` relate in concurrent UIs (urgent vs deferred)?", T, "hooks", ("usetransition", "deferred", "urgent"), "react", "t_defer"),
        (294, "What is `useSyncExternalStore` for (subscriptions, avoiding tearing with concurrent rendering)?", A, "hooks", ("usesyncexternalstore", "tearing", "store"), "react", "t_sync"),
        (295, "What is `useInsertionEffect` and why do CSS-in-JS libraries use it?", A, "hooks", ("useinsertioneffect", "css-in-js", "injection"), "react", "t_insert"),
        (296, "How can custom hooks help share stateful logic and composition in larger apps?", T, "hooks", ("custom-hook", "composition", "split"), "react", "t_cust"),
        (297, "What is `useDebugValue` and when is it most helpful for custom hook development?", T, "hooks", ("usedebugvalue", "devtools", "labels"), "react", "t_debug"),
        (298, "What belongs in a `useEffect` cleanup (subscriptions, timers) versus a component-wide singleton?", T, "hooks", ("cleanup", "teardown", "subscriptions"), "react", "t_dep"),
        (299, "What is the (experimental) 'use event' or stable-callback style pattern trying to improve for hooks code?", A, "hooks", ("experimental", "stable", "event"), "react", "t_exp"),
        (300, "What are solid best practices for using React hooks in production (linting, design, and performance)?", T, "hooks", ("best-practices", "review", "quality"), "react", "t_best"),
    ]


TEMPLATES: dict = {}


def _load_templates() -> None:
    global TEMPLATES
    TEMPLATES = {
        "t_mobx": (
            "Answer **{q}** by defining **observable** state, **actions** that change it, **derivations (computed)**, and **reactions** (for example a React component body as a **tracking** function) that re-run when **dependencies** they read change.\n\n"
            "Contrast **imperative** ad-hoc `set` calls everywhere with a **conventional** `action` and **reaction** network that is still testable, but **opinionated** in style versus **Redux**'s one-direction event log. Point to a **data-fetching** layer (TanStack Query) for **server** data even when the client state is **MobX**-backed in some apps."
        ),
        "t_state": (
            "Frame **{q}** as a *modeling* question about **global app state and predictability**.\n\n"
            "Explain **unidirectional, explicit updates** in Redux (actions, reducers, a single store) versus **reactive, observable** fields in MobX (actions, derivations) and how re-renders or subscriptions are triggered.\n\n"
            "Mention a **concrete** trade: Redux suits **loggable, time-travel** friendly flows, while MobX can reduce boilerplate in **interactive** UIs when teams adopt its **discipline** for actions and side effects. Point to a **data-fetching** layer (RTK Query, TanStack Query) as complementary."
        ),
        "t_js": (
            "**{q}** is best answered with a learning-path mindset.\n\n"
            "Modern **JavaScript (modules, const/let, arrow functions, destructuring, async/await, and Promises)** is the everyday syntax React examples assume, so a short ES6+ ramp reduces friction while you learn component thinking.\n\n"
            "State clearly that **you do not need to master every** API before Hello World, but you should be comfortable with **array/object basics and modules** to read app code. Link learning to the **TypeScript** step most teams add next."
        ),
        "t_conc": (
            "For **{q}**, focus on the **goals: interruptible, priority-aware** rendering to keep the UI responsive, coordinated with a **scheduling** system.\n\n"
            "**Concurrent** features let React **work on more than one conceptual priority** and yield so urgent updates (typing) are not starved by heavy trees. The older *async* naming sometimes referred to **time-slicing** language before the stable concurrent story landed.\n\n"
            "Name **Suspense, transitions, and deferred value** as user-visible outcomes, and say **the implementation is Fiber and its scheduler** under the hood."
        ),
        "t_sec": (
            "Answer **{q}** with a **safety and consistency** focus.\n\n"
            "React made **javascript:** URLs a louder footgun in attributes because they can be **XSS vectors**; prefer **data attributes + handlers**, **Trusted Types**, or a safe URL policy over inline JS URLs. Teach that **CSP, sanitization, and avoiding string-to-code** in attributes are a defense-in-depth set.\n\n"
            "For interviews, you show you connect **API misuse** in JSX attributes to the **browser** execution model, not just React re-renders."
        ),
        "t_lint": (
            "When interviewers ask **{q}**, they want the **plugin pair**: **`rules-of-hooks`** (hook order) and usually **`exhaustive-deps`** (stale/invalid effects) or your chosen equivalent.\n\n"
            "Explain the **developer loop**: ESLint in editor + CI, and the human step of not silencing a dependency without a real reason. Mention **TypeScript** as complementary static signal.\n\n"
            "Cite a **bug class** the linter saved you from, such as a **conditional hook** or a **stale** callback from missing deps, for credibility."
        ),
        "t_style": (
            "**{q}** is the classic *React philosophy* card.\n\n"
            "Contrast **imperative** (step-by-step DOM and event code) with **declarative** (describe the UI for each state, let React **reconcile**). The gain is **local reasoning** in components and a **data-first** test story.\n\n"
            "Acknowledge **escape hatches** (refs) when you *must* be imperative, but keep them **thin and labeled** in reviews."
        ),
        "t_ts": (
            "Open **{q}** with **type safety, refactor cost, and editor tooling**.\n\n"
            "TypeScript adds **static checks** to props, event handlers, reducers, and API shapes; it is especially valuable as **codebases and teams** grow. In interviews, you can speak to **strictness**, `unknown` over `any`, and **generated** or **Zod-typed** IO boundaries with React."
        ),
        "t_ts2": (
            "For **{q}**, use **inference, generics, and explicit unions**.\n\n"
            "Examples: `useState<User | null>`, `useState<Status>('idle' | 'done')`, or **tuple** state. Explain how **TypeScript 5+** quality-of-life in JSX helps avoid obvious prop mistakes.\n\n"
            "Tie the answer to **one real bug** you prevented at compile time (bad prop, impossible state), not a slogan."
        ),
        "t_auth": (
            "Approach **{q}** as **architecture + security** together.\n\n"
            "Use **Context** to expose **user identity, role, and an auth client** that can refresh a token in one place, often paired with a **BFF, cookies, or httpOnly** token strategy instead of a giant token in localStorage if your threat model needs it. Refresh flows usually **re-fetch session** and **re-render a minimal subtree** of providers.\n\n"
            "Name **a race**: parallel requests during refresh, and a **queue or single-flight** fix so UI does not flash logged-out states spuriously."
        ),
        "t_jsx": (
            "Explain **{q}** with the **dev surface area** in mind: **less React import noise**, and **automatic runtime** for JSX in modern Babel/TypeScript and bundler stacks.\n\n"
            "Benefits: smaller boilerplate, clearer tree-shaking story for certain setups, and better alignment with **the JSX runtime** import path. The older style often required a **transpiler option** to inject `import React` in scope.\n\n"
            "End with: **the JSX you write is the same; the transform changed**; consult your `tsconfig`/`babel` to match your framework (Create React App, Vite, Next) defaults."
        ),
        "t_rsc": (
            "Answer **{q}** as **server and client** responsibilities.\n\n"
            "**RSC** lets a framework stream **server React trees** to the client and pair them with **client** interactive islands, shrinking unnecessary JS when done right. The exact mental model and bundling rules are **framework-specific** (Next App Router, and so on).\n\n"
            "Avoid magical claims: show you know you still need a **data boundary**, **caching** story, and **serialization** rules for what crosses the wire, and you read `react.dev` and your **framework docs** together."
        ),
        "t_props": (
            "Use **{q}** to talk about **wiring** vs **re-use** cost.\n\n"
            "Prop drilling is passing props through layers that do not *use* them, only to reach a child. It is not automatically wrong, but it **signals a boundary** where **composition, context, or a small state module** may help. Avoid **global** everything on day one, but be honest at scale."
        ),
        "t_hookpair": (
            "For **{q}**, the crisp split is: **`useState` drives renders**; **`useRef` holds a mutable value without** scheduling a re-render for changes to `.current`.\n\n"
            "Typical `useRef` uses: **DOM node**, an **id**, **animation frame** handle, and **stale-avoiding** values that should not re-render. Use **state** for anything the user should **see** as updated UI (unless a specialist pattern needs otherwise). Mention **not** reusing a ref to replace state just to 'avoid renders' of legitimate UI data."
        ),
        "t_pattern": (
            "Answer **{q}** with **HOC, render-props, and hooks** as historical layers. Wrappers are still useful to **add behavior** (data, logging, a11y) or **consistency** in design systems. Hooks often **replaced** many HOCs, but a **higher-level layout** is still a wrapper concept.\n\n"
            "Caution: accidental **indirection and prop shadowing** in deep HOC stacks is why new code favors **function composition** and custom hooks, not endless wrapping."
        ),
        "t_effect": (
            "Compare **{q}** with **timing to paint**.\n\n"
            "`useEffect` **runs after** paint, great for data fetching, subscriptions, and most browser-only work. `useLayoutEffect` **fires before** the browser paints, good for **measuring** DOM, synchronizing scroll or layout that must be **correct before the user sees** the frame, at the cost of **blocking** longer than `useEffect` if abused.\n\n"
            "SSR caveat: `useLayoutEffect` warns; prefer **`useEffect` on server** or a **useIsomorphic** pattern from your stack documentation."
        ),
        "t_class": (
            "Approach **{q}** as **era + constraints**.\n\n"
            "Modern work is **function components + hooks**; classes are **legacy, error boundaries (until a modern alternative), and third-party** surfaces. The mental map: **state and lifecycle** moved to hooks; **getDerivedStateFromError**-style work still leans to classes in some libraries.\n\n"
            "Show empathy for codebases you join mid-flight; mention **strangler refactors** of hot paths first."
        ),
        "t_strict1": (
            "Describe **{q}** with **intentional extra work in dev** to surface **impure** render logic and unsafe lifecycles, without lying about any guarantee in **production**.\n\n"
            "Double **render/effect** calls in dev are a **smoke test**; side effects must be **idempotent** or **guarded** by design. The benefit is **earlier** detection of **memory leaks, racey subscriptions**, and state updates that are not idempotent in concurrent rendering.\n\n"
            "Mention the **Remix/Next/CRA** default templates that enable it for local dev."
        ),
        "t_jsxrules": (
            "Hit **{q}** with **one root expression**, **camelCase** DOM props, **className** not `class`, **style objects**, and that **`{}` embeds** JS expressions, not `if` statements (use ternary or IIFE patterns sparingly, prefer factoring).\n\n"
            "Mention `key` rules for **lists** and the **key reset** idiom for some controlled sub-trees, not a random key for everything."
        ),
        "t_immut": (
            "Connect **{q}** to **compare-by-reference, pure reducers, time-travel**, and **predictable** updates. Show **shallow** copies with spread for objects, **map/filter/concat** for arrays, and **structural sharing** in libraries like Immer when trees are deep or frequent.\n\n"
            "Call out a **bug** you fixed by stopping **in-place** mutation that skipped re-renders or broke memoization in parent props."
        ),
        "t_immer": (
            "Explain **{q}** as **syntactic sugar over structural sharing** that keeps **immutable** semantics while you write a **mutative** draft. Pair with a note that the **reducer** should still be **pure of async** side effects and that you understand **patches and produce** in larger apps.\n\n"
            "Mention a **use case**: nested form trees or undo stacks where manual spreads would be too noisy at every node."
        ),
        "t_mutfree": (
            "Use **{q}** to speak about **Time Travel debugging**, **React.memo** and **referential** equality, and **concurrent** rendering not assuming a single run order for render.\n\n"
            "A stable **snapshot** of state is easier to **reason, log, and test**; mutations can hide *when* a change really happened, especially in async flows. Keep reducers and render **pure**; push IO to the edges."
        ),
        "t_dom": (
            "For **{q}**, name **capture → target → bubble** in the DOM, and in React, **`on*Capture`** prop variants when you need capture phase, rare but important for some **overlay, portal, and analytics** use cases. React **synthetic events** have evolved; confirm details with the React version in your app.\n\n"
            "Close with: **default** React handlers are **bubble** unless you add **Capture**."
        ),
        "t_recon": (
            "Walk **{q}** in **render → diff → commit** terms at interview depth.\n\n"
            "State change schedules an update, React runs your **function** (or class) to produce a **new element tree**, **reconciles** with the previous fiber tree, and **commits** host DOM updates in batches when appropriate. The **key** and **type** of nodes control reuse versus replacement."
        ),
        "t_batch": (
            "Answer **{q}** with **grouping** `setState` work into a **single re-render** when React can, **inside the same event or tick** in modern models.\n\n"
            "Contrast **pre-18** (manual `unstable_batchedUpdates` in some cases for async) with **18+ automatic batching** in more **async** contexts, while noting **concurrent** features add nuance. Name **a metric**: fewer **intermediate paints** in a double-click handler."
        ),
        "t_ssr": (
            "Explain **{q}** as: server sends **HTML+payload**, client **hydrates** to attach event listeners and **activate** a client tree, often with **mismatches** as a class of bug if the HTML and client props diverge. Frameworks (Next) add **opinion** on **streaming, Suspense, and RSC**.\n\n"
            "Be explicit: **mismatch warnings** and **seeding** client stores from the server to avoid a flash."
        ),
        "t_inner": (
            "Use **{q}** to describe **re-created component types** each render, **state reset**, and **wasted** work for memoized children, versus **static** subcomponents in module scope. If you must define inline, **stabilize** with `useCallback`+`useMemo` carefully or extract.\n\n"
            "A common interview win is naming **a real bug** from inline components breaking **focus** or **animation**."
        ),
        "t_keys": (
            "Answer **{q}** with **identity** in React's world: a **key** nudges React about **sibling** identity, but any **remounting** use case that needs to **drop internal state** can sometimes use a **key on a sub-tree** to force reset, not just lists.\n\n"
            "Warn: **index keys** are unsafe when the list reorders, mutates, or is filtered, because **identity** and focus move incorrectly."
        ),
        "t_ured": (
            "Center **{q}** on **pure, synchronous** `state, action => next` functions and **one dispatch** pipeline. A reducer **aggregates** related updates, **versionable** in DevTools, and can scale to **action unions** in TypeScript.\n\n"
            "Clarify **no async** side effects in the reducer: keep IO in **thunks, sagas, RTK, `useEffect`**, or a **query** library."
        ),
        "t_uredctx": (
            "Tie **{q}** to a **lightweight** client store: a **reducer** + **Context Provider** to share **dispatch** and **state** without Redux. Tradeoffs: **re-render** scope if you do not **split** contexts, **value identity** on providers, and **no built-in** middleware the way Redux has.\n\n"
            "Good for **workshop-scale** apps, often replaced by a **global** solution when DevTools, middleware, and big teams need structure."
        ),
        "t_asyncred": (
            "Clarify **{q}** with **orchestrator** layers. Keep reducers **pure**; do async in **`useEffect`**, a **thunk** middleware, **RTK** async slices, or **Saga/Observable** in legacy stacks, then **dispatch** plain **actions** with results. Tests then target **orchestrators and reducers** separately.\n\n"
            "Cite a **two-step** flow: *loading* then *success/error* as explicit actions, not a thrown result inside a reducer case."
        ),
        "t_ctxex": (
            "For **{q}**, show **createContext** default, a **Provider** with **typed value**, and several **useContext** consumers, ideally **split** read vs write to reduce re-renders. Mention a **ref** or **useReducer** for high-frequency **dispatch** patterns.\n\n"
            "A tiny **codesandbox** shape is enough: **theme** or **locale** is the usual teaching example."
        ),
        "t_ctxp": (
            "Dissect **{q}** with **identity**: `value={{a,b}}` each render is a **new object** → **all** context consumers re-render, even if a deep field is unchanged, unless you **stabilize** (split contexts, `useMemo` value with careful dependencies, or smaller providers).\n\n"
            "Mention a **defensive default** in `createContext` to avoid `undefined` surprises and **optional** hook wrappers that `throw` when missing a provider in dev."
        ),
        "t_ctx": (
            "For **{q}**, set **rare, stable** or **broad** values: **theme, direction, i18n, current user** identity (not a changing cart line-item stream unless carefully sliced). `useContext` is a **read**; updates flow when **Provider** value **changes** per React rules.\n\n"
            "Contrasts to **Jotai/Zustand/Redux/Query** for different shapes of 'global' data, without holy wars."
        ),
        "t_dep": (
            "Train **{q}** to **synchronize** effect body with the **latest** state and props. **Empty** array means *mount-only*; **omitted** means *every* render (rare, sometimes for measuring). A wrong dep **array** is the **#1** subtle bug: stale closures, missing cleanup, and race conditions.\n\n"
            "Pair the answer with **eslint** + **human** review, because a correct dependency list is not only mechanical."
        ),
        "t_async2": (
            "Answer **{q}** with an **aborted** flag, **`AbortController`**, or a **canceled** boolean set in `cleanup` so late responses do not **set state** after unmount. Show **idempotent** fetches; avoid **async** *directly* in the `useEffect` callback's **sync** return slot—use an inner `async` IIFE you control.\n\n"
            "Name a **stale** UI bug a race caused in your work or a test you wrote to lock behavior."
        ),
        "t_layout": (
            "On **{q}**, reiterate: **synchronous to layout, before paint**; use for **measure + write** patterns that need **one** consistent frame, but not for **all** I/O. Overuse can **block** the main thread longer; prefer **`ResizeObserver`/`getBoundingClientRect` patterns** in careful order.\n\n"
            "Compare an example of **flicker** that `useLayoutEffect` fixed versus moving work to `useEffect` for non-visual side effects."
        ),
        "t_layout2": (
            "Cover **{q}** with the **no-op or warning** on the server, use **`useEffect` substitute** in SSR, and **isomorphic** helper hooks from the ecosystem. The goal is: **no layout reads** that assume **DOM** exists during server render or early pass.\n\n"
            "Link to a **bug class**: **hydration** mismatch if layout measurement ran only on the client in a way that differed from server HTML."
        ),
        "t_perf": (
            "Tackle **{q}** with **read/write** interleaving: reading layout, then mutating, then reading again **forces** extra layout passes. React batches many updates, but **imperative** DOM in effects still can thrash if you are not **batching** reads/writes. Tools: **`requestAnimationFrame`**, `ResizeObserver`, and **separating** measure from set style.\n\n"
            "Connect to `useLayoutEffect` **as a last resort** for tiny synchronous corrections, not a performance silver bullet."
        ),
        "t_ref1": (
            "Illustrate **{q}** with **`useRef<HTMLInputElement | null>(null)`**, attach **`ref`**, and call **`el.focus()` in `useEffect`** on mount or when enabled. Distinguish **uncontrolled** focus tasks from **fully controlled** state for **input value** itself.\n\n"
            "Note **string refs** in legacy code, but prefer **object refs** in modern function components."
        ),
        "t_ref2": (
            "Address **{q}** with **a ref to hold a previous render value**, updated in **`useEffect` after** render, or a **custom hook** `usePrevious`. Avoid **updating a ref in render** for values that *should* re-render the UI, because you would hide updates.\n\n"
            "Good use: **comparing** props with prior for **animations**, **imperative** diffs, or **logging** that should not re-render the tree on every print."
        ),
        "t_imph": (
            "Explain **{q}** with **hiding** imperative DOM/animation method soup behind a **small** imperative surface your parent needs. Pair with `forwardRef` to **receive** a ref from the parent, then `useImperativeHandle` to **expose a stable API** object.\n\n"
            "Warn: **leaky** imperative APIs complicate **testing**; prefer **declarative props** when possible; imperative for **genuine** integration (maps, text editors, media)."
        ),
        "t_memo2": (
            "Disambiguate **{q}** with `useMemo` for **values**, `useCallback` for **function identity**; both require **true dependencies**. **Neither** is a child memo replacement by itself: children need **`React.memo`** and **prop stability**; context changes still **invalidate** as usual.\n\n"
            "Anti-pattern: `useCallback` for **every** inline handler without measuring—**profile** first, then stabilize hot paths or split components."
        ),
        "t_cust": (
            "Define **{q}** as **a function starting with `use` that may call other hooks**—a reusable **stateful** unit. Rules: **only call** hooks at top level, **only** from functions that themselves obey the Rules of Hooks, and use **naming** that signals a hook. Great for **auth, data, forms**, and a11y behaviors.\n\n"
            "Compare **HOCs** and **children render props** as older composition styles."
        ),
        "t_fiber": (
            "For **{q}**, use **one paragraph**: Fiber is a **unit of work** in React's **incremental** reconciler, enabling **interruptible** rendering, **priorities**, and **suspense** coordination. The implementation detail is *not* your daily API, but it explains **concurrent** behavior at panels.\n\n"
            "Avoid 'virtual DOM' hand-waving: talk **tree of fibers, effects, and commit** instead."
        ),
        "t_useid": (
            "Answer **{q}** with **unique and stable** IDs across **SSR+CSR** to wire **for/id**, **ARIA** attributes, and **label** associations, without **hydration** mismatches a counter in render can cause. The hook returns a string safe for a **component instance**; consult docs for **multiple IDs** in one component (prefixing).\n\n"
            "Differentiate from **key**: **identity** in lists/reset vs **ID** in HTML attrs."
        ),
        "t_defer": (
            "Tie **{q}** to **keeping primary input** responsive while a **heavier** derived view catches up, often with **concurrent** scheduling. `useTransition` marks a **low priority** state update, while `useDeferredValue` **lags** a value to avoid blocking typing.\n\n"
            "Cite a **concrete** UX: **filtering 10k rows** while a text box remains instant."
        ),
        "t_sync": (
            "Explain **{q}** as the **store subscription** API that is **safe in concurrent** rendering, avoiding **tearing** (reading half-updated state). Classic example: an **external** Redux store or a **browser** API. Compare to **poor** hand-rolled `useLayoutEffect` subscriptions without proper integration.\n\n"
            "This is a **library author**-leaning question; show you read `react.dev` API notes, not a blog post title only."
        ),
        "t_insert": (
            "Cover **{q}** as **insertion timing before** layout effects for **injecting** global styles in **CSS-in-JS** with correct **cascade** order, **without** the flicker a naive `useEffect` might cause. Most app code will not author this; **style libraries** do.\n\n"
            "If you are not a library author, a crisp answer + pointer to a **package doc** is enough."
        ),
        "t_debug": (
            "On **{q}**, `useDebugValue` adds **lightweight** labels for **custom hooks** in **React DevTools** without affecting production unless polyfilled. Great for **library** hooks, sometimes noisy for every internal hook. Keep the **string small**; lazy formatting via a function second argument when expensive.\n\n"
            "Not a product feature for end users, only a **dev** affordance."
        ),
        "t_exp": (
            "Handle **{q}** with **caution: experimental, ecosystem**, and a **UX** need: a **callback** with **fresh** props without **changing identity** on every render, to fix **stale** closures in *some* event handlers. Today many teams use **`useEvent` patterns** in libraries or a **ref + wrapper** in app code, pending stable APIs.\n\n"
            "Never ship production behavior that depends on an **unstable** API without a hard pin and a migration plan."
        ),
        "t_best": (
            "Close the set on **{q}** with **lint+CI, pure renders, colocate** state, **measure** then memo, **separate** server cache from local UI, **one responsibility** per `useEffect`, and **name** custom hooks. Encourage **code review** checklists, **Storybook+RTL** tests for critical flows, and **type safety** in TS for props and **URL state** in routers.\n\n"
            "Be explicit: **context is not a global dump**, **Redux/Query** for different needs, and **suspense** for loading UX where supported."
        ),
        "t_rules": (
            "Hit **{q}** with the **top-level, stable order** rule; **class components** cannot use hooks, so the **refactor** path is a **new function wrapper** (or a **bridge** pattern) that composes a hook and passes data down, or a **gradual** migration for hot files.\n\n"
            "If you *must* interop, a **child function component** can host hooks, used by a class parent, but the shape gets awkward—prefer moving **forward**."
        ),
        "t_upd": (
            "Describe **{q}** for **stale** increments and **batched** updates. Functional updates **`s => s+1`** read the **latest** state when multiple sets happen in a handler. **Initializers** `useState(() => readStorage())` run **once** to avoid re-running expensive or non-idempotent work each render."
        ),
        "t_async": (
            "Tackle **{q}** with **no promise from `setState`**, and **observing** updates on the *next* render, not the next line of JS. Batching and **concurrent** rendering mean you **do not** assume immediate DOM or state reflect after a `set*`. The functional updater and **`useEffect`** for reactions are the usual tools.\n\n"
            "A classic pitfall: **if (state) fetch** in render based on a **just** set value—restructure to **useEffect** with deps or **derive** during render with previous props."
        ),
        "t_int": (
            "On **{q}**, stay at **fiber + hooks list** depth: a **per-component** **hooks dispatcher** and **memoized** state cells stored on the **fiber** for `useState` and friends. The exact implementation is private and **version** specific; avoid claiming **array index** is the *only* model—**debug hooks** in DevTools are your evidence.\n\n"
            "Good sign-off: 'I do not need to reimplement the scheduler; I use the public `use` APIs correctly.'"
        ),
        "t_next": (
            "Map **{q}** to **file-system first routing, layouts, and React Server** story in the **App Router**, versus the **imperative** `pages` directory model and **getServerSideProps** patterns in **Pages** router. The migration is a **long** planning topic; keep the **interview** answer to **user-visible** diffs: **nested** layouts, **loading** segments, and **RSC** defaults.\n\n"
            "Link to `nextjs.org` for **your** current major, because the surface shifts with releases."
        ),
        "t_memo": (
            "Answer **{q}** with **true expensive work** or **stabilized** derived props as `useMemo` candidates; **not** a band-aid for a **giant** render tree. Profile first; often **splits** in components or a **data layer** fix more than a memo. Remember **reference** identity still matters to memoized **children**.\n\n"
            "A quick anti-pattern: `useMemo` with **incomplete** deps and **stale** output—worse than no memo at all."
        ),
    }


def _links() -> dict:
    return {
        "mobx": ("MobX: introduction", "https://mobx.js.org/README.html#introduction"),
        "redux": ("Redux: core concepts", "https://redux.js.org/understanding/core-concepts/what-is-redux"),
        "mdn": ("MDN: JavaScript modules", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules"),
        "react": ("React: docs home", "https://react.dev"),
        "eslint": ("eslint-plugin-react-hooks", "https://www.npmjs.com/package/eslint-plugin-react-hooks"),
        "ts": ("TypeScript: React in TS", "https://www.typescriptlang.org/docs/handbook/react.html"),
        "next": ("Next.js: App Router", "https://nextjs.org/docs/app"),
    }


def build_ch2(item, ex) -> list:
    _load_table()
    _load_templates()
    L = _links()
    out = []
    for row in TABLE:
        idn, q, diff, cat, tag3, lkey, tpl = row
        body = TEMPLATES[tpl]
        # Use replace, not str.format, so literal `{}` in teaching text is safe.
        ans = body.replace("{q}", q)
        lab, href = L.get(lkey, L["react"])
        code = (
            "import { useState } from 'react';\n\n"
            f"// Topic from question id react-{idn:03d}\n"
            "export function Demo() {\n  const [n, setN] = useState(0);\n"
            f"  return <button onClick={{() => setN(n + 1)}}>n={{n}}</button>;\n"
            "}\n"
        )
        exs = [
            ex(
                "Minimal working sketch",
                "tsx",
                code,
                "A tiny stateful example you can map to the interview topic; adapt imports and effect placement for your stack.",
            )
        ]
        out.append(
            item(
                idn,
                q,
                diff,
                cat,
                list(tag3),
                ans,
                exs,
                f"Relate **{tag3[0]}** in your most recent app and name one test or user-visible outcome you would monitor.",
                lab,
                href,
            )
        )
    return out
