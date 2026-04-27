import { KataChallengeCard } from '@/components/technology/KataChallengeCard'
import { KataItem } from '@/components/technology/moduleData.types'

interface KataModuleSectionProps {
  items: KataItem[]
}

export const KataModuleSection = ({ items }: KataModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item, index) => (
      <KataChallengeCard
        key={item.id}
        item={item}
        number={index + 1}
      />
    ))}
  </div>
)
