import { useCallback } from "react";

/**
 * A flexible `Viewport` component that renders a `div` element and optionally centers its content.
 * It supports all standard HTML `div` attributes and an additional `fullyCentered` prop.
 *
 * @component
 * @param {Object} props - The component props.
 * @param {boolean} [props.fullyCentered=false] - If `true`, centers the content both horizontally and vertically using Flexbox.
 * @param {React.HTMLAttributes<HTMLDivElement>} props - Standard HTML div attributes.
 * @returns {JSX.Element} The rendered `Viewport` component.
 */
export const Viewport = (
  props: React.HTMLAttributes<HTMLDivElement> & { fullyCentered?: boolean }
) => {
  /**
   * Builds the style object dynamically based on the `fullyCentered` prop.
   *
   * @returns {React.CSSProperties} The computed styles.
   */
  const buildStyles = useCallback(
    (): React.CSSProperties => ({
      ...(props.fullyCentered
        ? {
            justifyContent: "center",
            alignItems: "center",
          }
        : {}),
        width: "100%",
        height: "100%",
    }),
    [props.fullyCentered]
  );

  return (
    <div
      {...props}
      className={props.className}
      style={{ ...props.style, ...buildStyles() }}
    ></div>
  );
};
