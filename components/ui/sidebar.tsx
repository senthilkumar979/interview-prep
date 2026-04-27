/**
 * Interview Forge app sidebar (shadcn pattern, split modules for maintainability).
 *
 * - Wrap the app in `SidebarProvider`, render `Sidebar` + `SidebarInset` siblings.
 * - Mobile: `Sidebar` becomes a sheet; desktop: fixed rail with offcanvas/icon modes.
 * - Toggle: `SidebarTrigger` or ⌘/Ctrl+B.
 *
 * @see https://ui.shadcn.com/docs/components/sidebar
 */
export {
  SIDEBAR_WIDTH,
  SIDEBAR_WIDTH_ICON,
  SIDEBAR_WIDTH_MOBILE,
  SidebarProvider,
  useSidebar,
} from "@/components/ui/sidebar/context"
export { Sidebar, SidebarInput, SidebarInset, SidebarTrigger } from "@/components/ui/sidebar/shell"
export {
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupAction,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarRail,
  SidebarSeparator,
} from "@/components/ui/sidebar/structure"
export {
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  sidebarMenuButtonVariants,
} from "@/components/ui/sidebar/menu"
export {
  SidebarMenuSkeleton,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from "@/components/ui/sidebar/menu-sub"
