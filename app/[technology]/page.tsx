import { notFound } from "next/navigation";
import { TechnologyCategory } from "@/components/home/technology.types";
import { TechnologyWorkspace } from "@/components/technology/TechnologyWorkspace";
import technologies from "@/content/technologies.json";

const technologyList = technologies as TechnologyCategory[];

export function generateStaticParams() {
  return technologyList.map((technology) => ({ technology: technology.slug }));
}

interface TechnologyPageProps {
  params: { technology: string };
}

export default function TechnologyPage({ params }: TechnologyPageProps) {
  const technology = technologyList.find((entry) => entry.slug === params.technology);
  if (!technology) notFound();

  return <TechnologyWorkspace technology={technology} />;
}
