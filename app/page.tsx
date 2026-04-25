import { TechnologyCatalog } from "@/components/home/TechnologyCatalog";
import { TechnologyCategory } from "@/components/home/technology.types";
import technologies from "@/content/technologies.json";

export const dynamic = "force-static";

export default function Home() {
  return <TechnologyCatalog technologies={technologies as TechnologyCategory[]} />;
}
