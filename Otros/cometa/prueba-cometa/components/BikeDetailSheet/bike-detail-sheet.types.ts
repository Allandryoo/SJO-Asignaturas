import type { Bike } from "@/components/BikeMap/bike-map.types";

export interface BikeDetailSheetProps {
  open: boolean;
  bike: Bike | null;
  handleOpenChange: (open: boolean) => void;
}

export interface BikeDetailHeaderProps {
  bike: Bike;
}

export interface BikeDetailContentProps {
  bike: Bike;
  formattedReservedUntil: string | null;
}

export interface BikeDetailFooterProps {
  bike: Bike;
  isLoading: boolean;
  errorMessage: string | null;
  isSuccess: boolean;
  onReserveClick: () => void;
}

