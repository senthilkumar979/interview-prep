import { KataItem } from "@/components/technology/moduleData.types";
import { KataChallengeCard } from "@/components/technology/KataChallengeCard";

interface KataModuleSectionProps {
  items: KataItem[];
}

export const KataModuleSection = ({ items }: KataModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item) => (
      <KataChallengeCard key={item.id} item={item} />
    ))}
  </div>
);
