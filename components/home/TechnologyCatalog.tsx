import { TechnologyCard } from "@/components/home/TechnologyCard";
import { TechnologyCategory } from "@/components/home/technology.types";

interface TechnologyCatalogProps {
  technologies: TechnologyCategory[];
}

export const TechnologyCatalog = ({ technologies }: TechnologyCatalogProps) => (
  <main className="min-h-svh bg-background px-4 py-8 sm:px-6 lg:px-10">
    <section className="mx-auto flex w-full max-w-6xl flex-col gap-6">
      <header className="rounded-lg border border-border/70 bg-card p-5">
        <p className="text-xs uppercase tracking-wide text-muted-foreground">Interview Forge</p>
        <h1 className="mt-2 text-3xl font-semibold tracking-tight">Technology Categories</h1>
        <p className="mt-2 max-w-3xl text-sm text-muted-foreground">
          Select a technology to open an IDE-style preparation space with categorized questions and exercises.
        </p>
      </header>

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {technologies.map((technology) => (
          <TechnologyCard key={technology.slug} technology={technology} />
        ))}
      </div>
    </section>
  </main>
);
