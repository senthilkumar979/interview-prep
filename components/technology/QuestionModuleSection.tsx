import { QuestionItem } from "@/components/technology/moduleData.types";
import { QuestionCard } from "@/components/technology/QuestionCard";

interface QuestionModuleSectionProps {
  items: QuestionItem[];
}

export const QuestionModuleSection = ({ items }: QuestionModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item) => (
      <QuestionCard key={item.id} item={item} />
    ))}
  </div>
);
