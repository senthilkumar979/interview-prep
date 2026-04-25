import Link from "next/link";
import { Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator } from "@/components/ui/breadcrumb";

interface BreadcrumbEntry {
  label: string;
  href?: string;
}

interface AppBreadcrumbsProps {
  items: BreadcrumbEntry[];
}

export const AppBreadcrumbs = ({ items }: AppBreadcrumbsProps) => (
  <Breadcrumb>
    <BreadcrumbList>
      {items.map((item, index) => {
        const isLastItem = index === items.length - 1;
        return (
          <BreadcrumbItem key={`${item.label}-${index}`}>
            {item.href && !isLastItem ? (
              <BreadcrumbLink asChild>
                <Link href={item.href}>{item.label}</Link>
              </BreadcrumbLink>
            ) : (
              <BreadcrumbPage>{item.label}</BreadcrumbPage>
            )}
            {!isLastItem ? <BreadcrumbSeparator /> : null}
          </BreadcrumbItem>
        );
      })}
    </BreadcrumbList>
  </Breadcrumb>
);
